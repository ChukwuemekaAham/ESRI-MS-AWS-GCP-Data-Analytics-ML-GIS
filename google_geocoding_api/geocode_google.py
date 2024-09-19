import psycopg2
from psycopg2.extras import RealDictCursor
import requests
import json

# Database connection parameters
database_parameters = {
    'host': 'host_here',
    'port': 'port_here',
    'user': 'username_here',
    'password': 'password_here',
    'dbname': 'database_name_here'
}

# Google Geocoding API key
google_api_key = "google_api_key_here"

# Connect to the database
conn = psycopg2.connect(**database_parameters)
conn.autocommit = True
cursor = conn.cursor(cursor_factory=RealDictCursor)

def get_latitude_longitude(address, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": api_key
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()
        # print(data)

        if data["status"] == "OK":
            result = data["results"][0]
            location = result["geometry"]["location"]
            return {"latitude": location["lat"], "longitude": location["lng"]}
        else:
            return None  # Address not found
    except requests.exceptions.RequestException as e:
        print(f"Error making request to Google Geocoding API: {e}")
        return None

# Fetch addresses from the database
# change this portion according to your requirements. 
cursor.execute("SELECT dwasa_call_center_id, address from dwasa_call_center where geom is null")
addresses = cursor.fetchall()

if addresses:
    i = 0
    for address in addresses:
        i += 1
        print(f"Count: {i}")

        id = address['dwasa_call_center_id']
        problem_location = address['address']        
        lat_lng = get_latitude_longitude(problem_location, google_api_key)

        if lat_lng:
            geojson = {
                "type": "Point",
                "coordinates": [lat_lng['longitude'], lat_lng['latitude']]
            }

            geojson_str = json.dumps(geojson)

            query = f'''
                UPDATE dwasa_call_center 
                SET geom = ST_SetSRID(ST_GeomFromGeoJSON('{geojson_str}'), 4326) 
                WHERE dwasa_call_center_id = {id}
            '''
            cursor.execute(query)
            print(f"Coordinates for {problem_location}: {lat_lng}")
            print("---------------------")
        else:
            print(f"Failed to geocode: {problem_location}")
