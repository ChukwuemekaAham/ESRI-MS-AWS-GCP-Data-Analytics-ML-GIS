import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrameCollection
from awsglue.dynamicframe import DynamicFrame
from awsglueml.transforms import FillMissingValues

# Script: Finds any distinct rows from the .csv file that do not yet exist in the AWS Glue Data Catalog to append to the AWS Glue Data Catalog movies table in the transform-movies-db database
def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    # new dataframe from collection
    new_dynf = dfc.select(list(dfc.keys())[1])
    # old dataframe from the AWS Glue Data Catalog
    old_dynf = dfc.select(list(dfc.keys())[0])

    # convert dynamicframe to dataframe
    new_df = new_dynf.toDF()
    old_df = old_dynf.toDF()

    # print rows of new and old dataframes
    print("new dataframe")
    new_df.show(n=5, vertical=True, truncate=50)
    print("old dataframe")
    old_df.show(n=5, vertical=True, truncate=50)

    # find any destinct rows from the .csv file that do not yet exist in the AWS Glue Data Catalog
    if old_df.count() == 0:
        # if this is the first time the job runs, append the full set of new data
        update_df = new_df
    else:
        # else, if there is already data in the AWS Glue Data Catalog, find all of the data from the .csv file that is not already in the AWS Glue Data Catalog
        # the left_anti join removes all duplicate records
        # this data will be appended later in Node 8
        update_df = new_df.join(old_df, [new_df.rank == old_df.rank], how="left_anti")

    # print unique rows from new data
    print("unique rows")
    update_df.show(n=5, vertical=True, truncate=50)

    # convert changed dataframe to dynamic dataframe
    update_dynf = DynamicFrame.fromDF(update_df, glueContext, "changed")

    # return new dynamicframe collection with only the new results
    return DynamicFrameCollection({"update_dynf": update_dynf}, glueContext)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Node 1: Input data from the data/movies_csv/movies.csv file in the S3 bucket
S3_bucket_node_1 = glueContext.create_dynamic_frame.from_options(
    format_options={
        "quoteChar": '"',
        "withHeader": True,
        "separator": ",",
        "optimizePerformance": False,
    },
    connection_type="s3",
    format="csv",
    connection_options={
        "paths": [
            "s3://databucket-us-west-2-1453430398056634/data/movies_csv/movies.csv"
        ],
        "recurse": True,
    },
    transformation_ctx="S3_bucket_node_1",
)

# Node 2: Input data from the AWS Glue Data Catalog movies table in the transform-movies-db database
Amazon_S3_node_2 = glueContext.create_dynamic_frame.from_catalog(
    database="transform-movies-db",
    table_name="movies",
    transformation_ctx="Amazon_S3_node_2",
)

# Node 3: Fill missing values in the data from the .csv file
Fill_Missing_Values_node_3 = FillMissingValues.apply(
    frame=S3_bucket_node_1,
    missing_values_column="rating",
    transformation_ctx="Fill_Missing_Values_node_3",
)

# Node 4: Apply mapping to the data stored in the AWS Glue Data Catalog movies table in the transform-movies-db database
Change_Schema_Apply_Mapping_node_4 = ApplyMapping.apply(
    frame=Amazon_S3_node_2,
    mappings=[
        ("year", "long", "year", "bigint"),
        ("title", "string", "title", "string"),
        ("directors_0", "string", "directors_0", "string"),
        ("genres_0", "string", "genres_0", "string"),
        ("genres_1", "string", "genres_1", "string"),
        ("rank", "long", "rank", "bigint"),
        ("running_time_secs", "long", "running_time_secs", "bigint"),
        ("actors_0", "string", "actors_0", "string"),
        ("actors_1", "string", "actors_1", "string"),
        ("actors_2", "string", "actors_2", "string"),
        ("directors_1", "string", "directors_1", "string"),
        ("directors_2", "string", "directors_2", "string"),
        ("rating_filled", "double", "rating_filled", "double"),
    ],
    transformation_ctx="Change_Schema_Apply_Mapping_node_4",
)

# Node 5: Apply mapping to the data from the .csv file
Change_Schema_Apply_Mapping_node_5 = ApplyMapping.apply(
    frame=Fill_Missing_Values_node_3,
    mappings=[
        ("year", "string", "year", "bigint"),
        ("title", "string", "title", "string"),
        ("directors_0", "string", "directors_0", "string"),
        ("genres_0", "string", "genres_0", "string"),
        ("genres_1", "string", "genres_1", "string"),
        ("rank", "string", "rank", "bigint"),
        ("running_time_secs", "string", "running_time_secs", "bigint"),
        ("actors_0", "string", "actors_0", "string"),
        ("actors_1", "string", "actors_1", "string"),
        ("actors_2", "string", "actors_2", "string"),
        ("directors_1", "string", "directors_1", "string"),
        ("directors_2", "string", "directors_2", "string"),
        ("rating_filled", "string", "rating_filled", "double"),
    ],
    transformation_ctx="Change_Schema_Apply_Mapping_node_5",
)

# Node 6: Use the MyTransform script to find any distinct records from the new dataframe that are not already in the AWS Glue Data Catalog movies table in the transform-movies-db database. Then, return those records to be appended in Node 8.
CustomTransform_node_6 = MyTransform(
    glueContext,
    DynamicFrameCollection(
        {
            "Change_Schema_Apply_Mapping_node_4": Change_Schema_Apply_Mapping_node_4,
            "Change_Schema_Apply_Mapping_node_5": Change_Schema_Apply_Mapping_node_5,
        },
        glueContext,
    ),
)

# Node 7: Select the new records from the collection (all of the records in the 0 table from Node 6)
SelectFromCollection_node_7 = SelectFromCollection.apply(
    dfc=CustomTransform_node_6,
    key=list(CustomTransform_node_6.keys())[0],
    transformation_ctx="SelectFromCollection_node_7",
)

# Node 8: Append any new rows to the AWS Glue Data Catalog movies table in the transform-movies-db database
AWSGlueDataCatalog_node_8 = glueContext.write_dynamic_frame.from_catalog(
    frame=SelectFromCollection_node_7,
    database="transform-movies-db",
    table_name="movies",
    transformation_ctx="AWSGlueDataCatalog_node_8",
)

job.commit()
