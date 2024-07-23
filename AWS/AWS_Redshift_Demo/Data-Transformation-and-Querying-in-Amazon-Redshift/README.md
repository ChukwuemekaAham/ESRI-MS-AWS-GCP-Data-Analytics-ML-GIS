# Data Transformation and Querying in Amazon Redshift

This demonstrates Extract, Load and Transform (ELT) with Redshift Materialized Views and scheduled queries.

## Required
•	AdministratorPassword
•	CommandHostUrl
•	DataBucket
•	RedshiftRole
•	Region
•	ScheduledQueriesRole
 

## Objectives:
- Create an external table
- Create and query a materialized view
- Use Amazon Redshift data sharing for faster data access between clusters
- Schedule a query


QueryId=INSERT_QUERY_ID


aws sts assume-role --role-session-name AWSCLI-Session --role-arn INSERT_SCHEDULED_QUERIES_ROLE


export AWS_ACCESS_KEY_ID=INSERT_AccessKeyId
export AWS_SECRET_ACCESS_KEY=INSERT_SecurityAccessKey
export AWS_SESSION_TOKEN=INSERT_SessionToken

aws redshift-data get-statement-result --id $QueryId

```json

{
    "Records": [
        [
            {
                "stringValue": "aapl"
            },
            {
                "stringValue": "1021692400"
            }
        ],
        [
            {
                "stringValue": "tsla"
            },
            {
                "stringValue": "409559800"
            }
        ],
        [
            {
                "stringValue": "ge"
            },
            {
                "stringValue": "388263400"
            }
        ]
    ],
    "ColumnMetadata": [
        {
            "isCaseSensitive": true,
            "isCurrency": false,
            "isSigned": false,
            "label": "ticker",
            "length": 0,
            "name": "ticker",
            "nullable": 1,
            "precision": 5,
            "scale": 0,
            "schemaName": "public",
            "tableName": "mv_tbl__stocks_mv__0",
            "typeName": "varchar"
        },
        {
            "isCaseSensitive": false,
            "isCurrency": false,
            "isSigned": true,
            "label": "sum_volume",
            "length": 0,
            "name": "sum_volume",
            "nullable": 1,
            "precision": 38,
            "scale": 0,
            "schemaName": "",
            "tableName": "",
            "typeName": "numeric"
        }
    ],
    "TotalNumRows": 3
}


```