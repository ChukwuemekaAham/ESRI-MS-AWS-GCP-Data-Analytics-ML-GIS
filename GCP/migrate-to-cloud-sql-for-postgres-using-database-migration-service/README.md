# Configure a continuous Database Migration Service job to migrate databases from a PostgreSQL instance to Cloud SQL for PostgreSQL

In this demo, I migrated a stand-alone PostgreSQL database (running on a virtual machine) to Cloud SQL for PostgreSQL using a continuous Database Migration Service job and VPC peering for connectivity.

Database Migration Service provides options for one-time and continuous jobs to migrate data to Cloud SQL using different connectivity options, including IP allowlists, VPC peering, and reverse SSH tunnels see documentation on connectivity options at https://cloud.google.com/database-migration/docs/postgresql/configure-connectivity.

Migrating a database via Database Migration Service requires some preparation of the source database, including creating a dedicated user with replication rights, adding the pglogical database extension to the source database and granting rights to the schemata and tables in the database to be migrated, as well as the postgres database, to that user.

After creating and running the migration job, I confirmed that an initial copy of the database has been successfully migrated to the Cloud SQL for PostgreSQL instance. I also explored how continuous migration jobs apply data updates from a source database to target Cloud SQL instance. To conclude the migration job, I promoted the Cloud SQL instance to be a stand-alone database for reading and writing data.

## Objectives
•	Prepare the source database for migration.
•	Create a profile for a source connection to a PostgreSQL instance (e.g., stand-alone PostgreSQL).
•	Configure connectivity between the source and destination database instances using VPC peering.
•	Configure firewall and database access rules to allow access to the source database for migration.
•	Create, run, and verify a continuous migration job using Database Migration Service.
•	Promote the destination instance (Cloud SQL for PostgreSQL) to be a stand-alone database for reading and writing data.

- Enable the Database Migration API is 

**Task 1. Prepare the source database for migration**
- Adding support features to the source database which are required in order for Database Migration Service to perform a migration. These are:
•	Installing and configuring the pglogical database extension.
•	Configuring the stand-alone PostgreSQL database to allow access from Cloud Shell and Cloud SQL.
•	Adding the pglogical database extension to the postgres, orders and gmemegen_db databases on the stand-alone server.
•	Creating a migration_admin user (with Replication permissions) for database migration and granting the required permissions to schemata and relations to that user.

- Upgrade the database with the pglogical extension
Download and add the pglogical database extension to the orders and postgres databases on the postgresql-vm VM Instance using SSH

`sudo apt install postgresql-13-pglogical`

Note: pglogical is a logical replication system implemented entirely as a PostgreSQL extension. Fully integrated, it requires no triggers or external programs. This alternative to physical replication is a highly efficient method of replicating data using a publish/subscribe model for selective replication. Read more here: https://github.com/2ndQuadrant/pglogical

- Download and apply some additions to the PostgreSQL configuration files (to enable pglogical extension) and restart the postgresql service:

SEE: `./output.md` file for more information.