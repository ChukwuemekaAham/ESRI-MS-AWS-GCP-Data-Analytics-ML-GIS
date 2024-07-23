import sys, getopt
import random, json, string
import datetime
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
import time
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
import boto3

random_user_agent=''.join(random.choices(string.ascii_uppercase + string.digits, k=22))

def on_publish(client,userdata,result):             #create function for callback
    pass

def pick_weather(choice):
    if choice == 'Clear':
        return random.choice([ 'Clear', 'Sunny' ])
    elif choice == 'Rain':
        return random.choice([ 'Rain',  'Thunder & Lightning', 'Damaging Wind'])
    elif choice == 'Cloudy':
        return random.choice([ 'Cloudy', 'Heavy Fog'])
    elif choice == 'Snow':
        return random.choice([ 'Snow', 'Snow Storm'])
    else:
        return "Wrong entry"

def getFleetRegNo():
    # Generate 10 letter random alpha numeric ID
    return str(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10)))

def getId():
    # Generate 10 letter random numeric ID
    return random.choice(range(1000000000, 9999999999))

def prepareStaticDataForOneTrip(staticData):
    distributionCenterList = {
        "ODC Los Angeles": (34.05, -118.24),
        "ODC San Jose": (37.33, -121.89),
        "ODC Seattle": (47.60, -122.33),
        "ODC Portland": (45.52, -122.67),
        "ODC San Francisco": (37.77, -122.43),
        "ODC Las Vegas": (36.16, -115.13)
    }

    # Check if staticData already have something, if yes then it is next run and dest will become origin, else compute both as new
    if (not bool(staticData)):
        # Get origin and destination
        originODC = random.choice(list(distributionCenterList))
        # Generate random devide ID for test
        # keep the device id and fleet reg no same if it is second run
        staticData['deviceId'] = random.choice([ getId() ])
        staticData['fleetRegNo'] = random.choice([ getFleetRegNo() ])

        # Set default oil level in % from 0 - 1%, kibana will multiply by 100 to show as %, next trip will start with previous oil level
        # Generates random number b/w 0.0 to 1.0
        staticData['oilLevel'] = round(random.random(),2)
        staticData['milesTravelled'] = 0.0
        staticData['totalFuelUsed'] = 0.0

        # pick a random choice for career
        staticData['carrier'] = random.choice([ 'OpenSearch Van Lines', 'DataPrepper Logistics', 'Dashboards Logistics' ])

        staticData['temperature'] = random.choice(range(-10, 100))

    else:
        # Now destination would be current destination if this is second run
        originODC = staticData['destinationODC']

    # Trip ID
    staticData['tripId'] = random.choice([ getId() ])

    # Check random destination and ignore the origin
    destinationODC = random.choice([x for x in distributionCenterList if x != originODC])
    # initialize Nominatim API to fetch geo details from lat, lon
    geolocator = Nominatim(user_agent=random_user_agent)
    originLatLon = distributionCenterList[originODC]
    destinationLatLon = distributionCenterList[destinationODC]

    # Get origin and destination city, country ext from geoIP (Get data in JSON (if remove.raw['address']), it will print in plain line)
    originGeo = geolocator.reverse(originLatLon).raw['address']
    staticData['originODC'] = originODC
    staticData['originCountry'] = originGeo.get('country', '')
    staticData['originCity'] = originGeo.get('city', '')
    staticData['originState'] = originGeo.get('state', '')
    # Convert tuple to string and separate by comma, as needed by elastic geo_poiunt data type
    staticData['originGeo'] = ','.join(str(o) for o in originLatLon)

    destinationGeo = geolocator.reverse(destinationLatLon).raw['address']
    staticData['destinationODC'] = destinationODC
    staticData['destinationCountry'] = destinationGeo.get('country', '')
    staticData['destinationCity'] = destinationGeo.get('city', '')
    staticData['destinationState'] = destinationGeo.get('state', '')
    # Convert tuple to string and separate by comma, as needed by elastic geo_poiunt data type
    staticData['destinationGeo'] = ','.join(str(o) for o in destinationLatLon)

    # Distance between origin and dest in miles
    staticData['speedInMiles'] = 0
    staticData['distanceMiles'] = round(great_circle(originLatLon, destinationLatLon).mi, 2)
    staticData['milesToDestination'] = staticData['distanceMiles'] # Used for reducing miles over a period of time

def generate(client):
    # Prepare data dictionary
    staticData = {}
    actions = []
    i = 0
    # Run infinitely () 2-3 hrs gap b/w one trip and keep the device id and fleet reg no same
    while(True):
        prepareStaticDataForOneTrip(staticData)

        startTime = datetime.datetime.now()
        previousSpeedCheck = startTime
        previousTempCheck = startTime
        previousOilCheck = startTime

        # Iterate for one trip
        while(True):

            currTime = datetime.datetime.now()
            # Get current timestamp
            timestamp=datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
            indexName="opensearch-client-ingest-" +timestamp.split('T')[0]
            staticData['@timestamp']=timestamp
            # Change speed after X second
            if currTime >= previousSpeedCheck:
                constSpeedSec = random.choice(range(45, 60))
                previousSpeedCheck = currTime + datetime.timedelta(seconds=constSpeedSec)

                # For edge case if previous speed was > 72 then only fetch random again from 0, 100 else fetch from 0 to 75
                if staticData['speedInMiles'] > 70 and staticData['speedInMiles'] <= 75:
                    # Choose speed in the range of 0 - 90
                    constSpeed = random.choice(range(0, 100))
                else:
                    # Choose speed in the range of 0 - 90
                    constSpeed = random.choice(range(0, 75))

                staticData['speedInMiles'] = constSpeed

                # Calculating remaining distance to reach to dest
                distanceInThisSession = ( constSpeedSec * (constSpeed/3600) )
                staticData['milesTravelled'] = staticData['milesTravelled'] + distanceInThisSession
                staticData['milesToDestination'] = staticData['milesToDestination'] - distanceInThisSession

                # Set traffic level depending upon speed
                if constSpeed > 75:
                    staticData['traffic'] = "no"
                elif constSpeed <= 75 and constSpeed > 65:
                    staticData['traffic'] = "no"
                elif constSpeed <= 65 and constSpeed > 40:
                    staticData['traffic'] = "low"
                elif constSpeed <= 40 and constSpeed > 20:
                    staticData['traffic'] = "moderate"
                elif constSpeed <= 20:
                    staticData['traffic'] = "heavy"


            # Change temperature after 5-10 mins
            if currTime >= previousTempCheck:
                previousTempCheck = currTime + datetime.timedelta(minutes=random.choice(range(5, 10)))
                # Choose temp in the range of +-10 degree to previous temperature
                staticData['temperature'] = random.choice(range( max(staticData['temperature'] - 10, -10), min(staticData['temperature'] + 10, 105)))

                # Update weather details as per temperature and when temperature changes
                if staticData['temperature'] > 70:
                    staticData['weather_category'] = 'Clear'
                elif staticData['temperature'] <= 70 and staticData['temperature'] > 40:
                    staticData['weather_category'] = 'Rain'
                elif staticData['temperature'] <= 40 and staticData['temperature'] > 0:
                    staticData['weather_category'] = 'Cloudy'
                elif staticData['temperature'] <= 0:
                    staticData['weather_category'] = 'Snow'
            staticData['weather'] = pick_weather(staticData['weather_category'])

            # For Oil level every 8-12 min, reduce the oil level by 1%
            if currTime >= previousOilCheck:
                previousOilCheck = currTime + datetime.timedelta(minutes=random.choice(range(8, 12)))
                # If oil level comes below 15% re-fuel to 100%
                if staticData['oilLevel'] < 0.15:
                    staticData['oilLevel'] = 1
                else:
                    staticData['oilLevel'] = staticData['oilLevel'] - 0.01
                    # Historical fuel used
                    staticData['totalFuelUsed'] = staticData['totalFuelUsed'] + 0.01

            if(staticData['milesToDestination'] <= 0 ):
                # If fleet reached the destination, set the speed as 0, miles as 0, traffic as no
                staticData['traffic'] = "no"
                staticData['milesToDestination'] = 0
                staticData['speedInMiles'] = 0

                client.index(index=indexName,   body=(json.dumps(staticData)).encode('utf-8'))
                time.sleep(0.1)
                break
            else:
                action = {"index": {"_index": indexName}}
                actions.append(action)
                actions.append(staticData.copy())
                # 0.1 -> 100ms -> 10 EPS
                # 0.05 -> 50ms -> 20 EPS
                # 0.02 -> 20ms -> 50 EPS
                # 0.01 -> 10ms -> 100 EPS

                if(i <= 100 ):
                    time.sleep(0.1)
                    i += 1
                else:
                    print("\n=== sending bulk: " + str(len(actions)) + " documents")
                    print(actions[0])                    
                    response = client.bulk(body=actions)
                    if response["errors"] == False:
                        print("documents sent successfully")
                    else:
                        print(response)
                        exit()
                    actions = []
                    i = 0
        # After 1 trip sleep in between one to four minutes, before starting next trip
        time.sleep(random.choice(range(1, 4)))

def main(argv):
    host = ''
    region = 'us-east-1'

    opts, args = getopt.getopt(argv, "h:r:")
    for opt, arg in opts:
        if opt == '-h':
            host = arg
        elif opt == '-r':
            region = arg
    if host == '':
        print("required argument -h <Amazon OpenSearch Serverless host endpoint>")
        exit()

    service = 'aoss'
    credentials = boto3.Session().get_credentials()
    awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service,
                   session_token=credentials.token)
    # Build the OpenSearch client
    client = OpenSearch(
        hosts = [{'host': host, 'port': 443}],
        http_auth = awsauth,
        timeout = 300,
        use_ssl = True,
        verify_certs = True,
        connection_class = RequestsHttpConnection
    )
    print(f"OpenSearch Client - Sending to Amazon OpenSearch Serverless host {host} in Region {region} \n")
    generate(client)

if __name__ == '__main__':
    main(sys.argv[1:])
