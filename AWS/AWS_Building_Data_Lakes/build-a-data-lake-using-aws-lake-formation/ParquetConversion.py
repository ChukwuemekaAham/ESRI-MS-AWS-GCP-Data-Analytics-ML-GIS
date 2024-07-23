import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_catalog(
    database="movies-db", table_name="data", transformation_ctx="S3bucket_node1"
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("year", "long", "year", "long"),
        ("title", "string", "title", "string"),
        ("directors_0", "string", "directors_0", "string"),
        ("rating", "double", "rating", "double"),
        ("genres_0", "string", "genres_0", "string"),
        ("genres_1", "string", "genres_1", "string"),
        ("rank", "long", "rank", "long"),
        ("running_time_secs", "long", "running_time_secs", "long"),
        ("actors_0", "string", "actors_0", "string"),
        ("actors_1", "string", "actors_1", "string"),
        ("actors_2", "string", "actors_2", "string"),
        ("directors_1", "string", "directors_1", "string"),
        ("directors_2", "string", "directors_2", "string"),
        ("partition_0", "string", "partition_0", "string"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.write_dynamic_frame.from_options(
    frame=ApplyMapping_node2,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://databucket-us-east-1-2228993963339617/data/movies_parquet/",
        "partitionKeys": [],
    },
    format_options={"compression": "uncompressed"},
    transformation_ctx="S3bucket_node3",
)

job.commit()
