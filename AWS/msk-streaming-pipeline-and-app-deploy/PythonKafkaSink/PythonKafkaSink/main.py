from pyflink.table import EnvironmentSettings, StreamTableEnvironment, StatementSet
import os
import json

env_settings = EnvironmentSettings.new_instance().in_streaming_mode().use_blink_planner().build()
table_env = StreamTableEnvironment.create(environment_settings=env_settings)
statement_set = table_env.create_statement_set()

def create_table_input(table_name, stream_name, broker):
    return """ CREATE TABLE {0} (
                `Account_Id` BIGINT NOT NULL,
                `Customer_Name` VARCHAR(30) NOT NULL,
                `Transaction_Id` VARCHAR(20) NOT NULL,
                `Transaction_Date` TIMESTAMP(3),
                `Merchant_Type` VARCHAR(30) NOT NULL,
                `Transaction_Type` VARCHAR(30) NOT NULL,
                `Transaction_Amount` decimal(10,2) NOT NULL
              )
              WITH (
                'connector' = 'kafka',
                'topic' = '{1}',
                'properties.bootstrap.servers' = '{2}',
                'properties.group.id' = 'testGroup',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601',
                'scan.startup.mode' = 'latest-offset'
              ) """.format(table_name, stream_name, broker)

def create_table_input_flagged(table_name, stream_name, broker):
    return """ CREATE TABLE {0} (
                `Account_Id` BIGINT NOT NULL,
                `Flag_Date` TIMESTAMP(3)
              )
              WITH (
                'connector' = 'kafka',
                'topic' = '{1}',
                'properties.bootstrap.servers' = '{2}',
                'properties.group.id' = 'testGroup',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601',
                'scan.startup.mode' = 'latest-offset'
              ) """.format(table_name, stream_name, broker)

def create_table_output_kafka(table_name, stream_name, broker):
    return """ CREATE TABLE {0} (
                `Account_Id` BIGINT NOT NULL,
                `Customer_Name` VARCHAR(30) NOT NULL,
                `Transaction_Id` VARCHAR(20) NOT NULL,
                `Transaction_Date` TIMESTAMP(3),
                `Merchant_Type` VARCHAR(30) NOT NULL,
                `Transaction_Type` VARCHAR(30) NOT NULL,
                `Transaction_Amount` decimal(10,2) NOT NULL,
                `Flag_Date` TIMESTAMP(3)
              )
              WITH (
                'connector' = 'kafka',
                'topic' = '{1}',
                'properties.bootstrap.servers' = '{2}',
                'properties.group.id' = 'testGroup',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601'
              ) """.format(table_name, stream_name, broker)


def insert_stream_msk(insert_from,compare_with,insert_into):
    return """ INSERT INTO {2}
               Select a.*,b.Flag_Date
                FROM
                {0} AS a,
                {1} AS b
                WHERE a.Account_Id = b.Account_Id  and a.Transaction_Date >= b.Flag_Date
               """.format(insert_from,compare_with,insert_into)

def app_properties():
    file_path = '/etc/flink/application_properties.json'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            contents = file.read()
            print('Contents of ' + file_path)
            print(contents)
            properties = json.loads(contents)
            return properties
    else:
        print('A file at "{}" was not found'.format(file_path))


def property_map(props, property_group_id):
    for prop in props:
        if prop["PropertyGroupId"] == property_group_id:
            return prop["PropertyMap"]


def main():

    INPUT_PROPERTY_GROUP_KEY = "producer.config.0"
    CONSUMER_PROPERTY_GROUP_KEY = "consumer.config.0"

    INPUT_TOPIC_KEY = "input.topic.name"
    INPUT_TOPIC2_KEY = "input.topic2.name"  ## Added for flagged customer topic
    OUTPUT_TOPIC_KEY = "output.topic.name"

    BROKER_KEY = "bootstrap.servers"

    props = app_properties()

    input_property_map = property_map(props, INPUT_PROPERTY_GROUP_KEY)
    output_property_map = property_map(props, CONSUMER_PROPERTY_GROUP_KEY)

    input_stream = input_property_map[INPUT_TOPIC_KEY]
    input_stream2 = input_property_map[INPUT_TOPIC2_KEY] ## Added for flagged customer topic
    broker = input_property_map[BROKER_KEY]

    output_stream_msk = output_property_map[OUTPUT_TOPIC_KEY]


    input_table = "input_table"
    input_table2 = "input_table2"   ## Added for flagged customer topic
    output_table_msk = "output_table_msk"

    table_env.execute_sql(create_table_input(input_table, input_stream, broker))
    table_env.execute_sql(create_table_input_flagged(input_table2, input_stream2, broker))  ## Added for flagged customer topic

    table_env.execute_sql(create_table_output_kafka(output_table_msk, output_stream_msk, broker))

    print(insert_stream_msk(input_table,input_table2, output_table_msk))
    statement_set.add_insert_sql(insert_stream_msk(input_table,input_table2, output_table_msk))
    statement_set.execute()

if __name__ == '__main__':
    main()
