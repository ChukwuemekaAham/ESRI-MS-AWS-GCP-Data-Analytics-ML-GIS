```bash
student-04-9c778badac0d@postgresql-vm:~$ sudo apt install postgresql-13-pglogical
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following NEW packages will be installed:
  postgresql-13-pglogical
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
Need to get 424 kB of archives.
After this operation, 1200 kB of additional disk space will be used.
Get:1 http://apt.postgresql.org/pub/repos/apt buster-pgdg/main amd64 postgresql-13-pglogical amd64 2.4.2-2.pgdg100+1 [424 kB]
Fetched 424 kB in 1s (608 kB/s)             
Selecting previously unselected package postgresql-13-pglogical.
(Reading database ... 60251 files and directories currently installed.)
Preparing to unpack .../postgresql-13-pglogical_2.4.2-2.pgdg100+1_amd64.deb ...
Unpacking postgresql-13-pglogical (2.4.2-2.pgdg100+1) ...
Setting up postgresql-13-pglogical (2.4.2-2.pgdg100+1) ...
Processing triggers for postgresql-common (248.pgdg100+1) ...
Building PostgreSQL dictionaries from installed myspell/hunspell packages...
Removing obsolete dictionary files:
student-04-9c778badac0d@postgresql-vm:~$ ls
student-04-9c778badac0d@postgresql-vm:~$ sudo su - postgres -c "gsutil cp gs://cloud-training/gsp918/pg_hba_append.conf ."
Copying gs://cloud-training/gsp918/pg_hba_append.conf...
/ [1 files][   68.0 B/   68.0 B]                                                
Operation completed over 1 objects/68.0 B.                                       
student-04-9c778badac0d@postgresql-vm:~$ sudo su - postgres -c "gsutil cp gs://cloud-training/gsp918/postgresql_append.conf ."
Copying gs://cloud-training/gsp918/postgresql_append.conf...
/ [1 files][  543.0 B/  543.0 B]                                                
Operation completed over 1 objects/543.0 B.                                      
student-04-9c778badac0d@postgresql-vm:~$ sudo su - postgres -c "cat pg_hba_append.conf >> /etc/postgresql/13/main/pg_hba.conf"
student-04-9c778badac0d@postgresql-vm:~$ sudo su - postgres -c "cat postgresql_append.conf >> /etc/postgresql/13/main/postgresql.conf"
student-04-9c778badac0d@postgresql-vm:~$ sudo systemctl restart postgresql@13-main
student-04-9c778badac0d@postgresql-vm:~$ sudo su - postgres
postgres@postgresql-vm:~$ psql
psql (13.10 (Debian 13.10-1.pgdg100+1))
Type "help" for help.

postgres=# \c postgres;
You are now connected to database "postgres" as user "postgres".
postgres=# CREATE EXTENSION pglogical;
CREATE EXTENSION
postgres=# \c orders;
You are now connected to database "orders" as user "postgres".
orders=# CREATE EXTENSION pglogical;
CREATE EXTENSION
orders=# \c gmemegen_db;
You are now connected to database "gmemegen_db" as user "postgres".
gmemegen_db=# CREATE EXTENSION pglogical;
CREATE EXTENSION
gmemegen_db=# \l
                               List of databases
    Name     |  Owner   | Encoding | Collate |  Ctype  |   Access privileges   
-------------+----------+----------+---------+---------+-----------------------
 gmemegen_db | postgres | UTF8     | C.UTF-8 | C.UTF-8 | 
 orders      | postgres | UTF8     | C.UTF-8 | C.UTF-8 | 
 postgres    | postgres | UTF8     | C.UTF-8 | C.UTF-8 | 
 template0   | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
             |          |          |         |         | postgres=CTc/postgres
 template1   | postgres | UTF8     | C.UTF-8 | C.UTF-8 | =c/postgres          +
             |          |          |         |         | postgres=CTc/postgres
(5 rows)

gmemegen_db=# exit
postgres@postgresql-vm:~$ psql
psql (13.10 (Debian 13.10-1.pgdg100+1))
Type "help" for help.

postgres=# CREATE USER replication_admin PASSWORD 'DMS_1s_cool!';
CREATE ROLE
postgres=# ALTER DATABASE orders OWNER TO replication_admin;
ALTER DATABASE
postgres=# ALTER ROLE replication_admin WITH REPLICATION;
ALTER ROLE
postgres=# \c postgres;
You are now connected to database "postgres" as user "postgres".
postgres=# GRANT USAGE ON SCHEMA pglogical TO replication_admin;
GRANT
postgres=# GRANT ALL ON SCHEMA pglogical TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.tables TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.depend TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.local_node TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.local_sync_status TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.node TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.node_interface TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.queue TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.replication_set TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.replication_set_seq TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.replication_set_table TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.sequence_state TO replication_admin;
GRANT
postgres=# GRANT SELECT ON pglogical.subscription TO replication_admin;
GRANT
postgres=# \c orders;
You are now connected to database "orders" as user "postgres".
orders=# GRANT USAGE ON SCHEMA pglogical TO replication_admin;
GRANT
orders=# GRANT ALL ON SCHEMA pglogical TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.tables TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.depend TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.local_node TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.local_sync_status TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.node TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.node_interface TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.queue TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.replication_set TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.replication_set_seq TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.replication_set_table TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.sequence_state TO replication_admin;
GRANT
orders=# GRANT SELECT ON pglogical.subscription TO replication_admin;
GRANT
orders=# GRANT USAGE ON SCHEMA public TO replication_admin;
GRANT
orders=# GRANT ALL ON SCHEMA public TO replication_admin;
GRANT
orders=# GRANT SELECT ON public.distribution_centers TO replication_admin;
GRANT
orders=# GRANT SELECT ON public.inventory_items TO replication_admin;
GRANT
orders=# GRANT SELECT ON public.order_items TO replication_admin;
GRANT
orders=# GRANT SELECT ON public.products TO replication_admin;
GRANT
orders=# GRANT SELECT ON public.users TO replication_admin;
GRANT
orders=# \c gmemegen_db;
You are now connected to database "gmemegen_db" as user "postgres".
gmemegen_db=# GRANT USAGE ON SCHEMA pglogical TO replication_admin;
GRANT
gmemegen_db=# GRANT ALL ON SCHEMA pglogical TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.tables TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.depend TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.local_node TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.local_sync_status TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.node TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.node_interface TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.queue TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.replication_set TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.replication_set_seq TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.replication_set_table TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.sequence_state TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON pglogical.subscription TO replication_admin;
GRANT
gmemegen_db=# GRANT USAGE ON SCHEMA public TO replication_admin;
GRANT
gmemegen_db=# GRANT ALL ON SCHEMA public TO replication_admin;
GRANT
gmemegen_db=# GRANT SELECT ON public.meme TO replication_admin;
GRANT
gmemegen_db=# \c orders;
You are now connected to database "orders" as user "postgres".
orders=# \dt
                List of relations
 Schema |         Name         | Type  |  Owner   
--------+----------------------+-------+----------
 public | distribution_centers | table | postgres
 public | inventory_items      | table | postgres
 public | order_items          | table | postgres
 public | products             | table | postgres
 public | users                | table | postgres
(5 rows)

orders=# ALTER TABLE public.distribution_centers OWNER TO replication_admin;
ALTER TABLE
orders=# ALTER TABLE public.inventory_items OWNER TO replication_admin;
ALTER TABLE
orders=# ALTER TABLE public.order_items OWNER TO replication_admin;
ALTER TABLE
orders=# ALTER TABLE public.products OWNER TO replication_admin;
ALTER TABLE
orders=# ALTER TABLE public.users OWNER TO replication_admin;
ALTER TABLE
orders=# \dt
                    List of relations
 Schema |         Name         | Type  |      Owner      
--------+----------------------+-------+-----------------
 public | distribution_centers | table | replication_admin
 public | inventory_items      | table | replication_admin
 public | order_items          | table | replication_admin
 public | products             | table | replication_admin
 public | users                | table | replication_admin
(5 rows)

orders=# \q
postgres@postgresql-vm:~$ exit
logout
student-04-9c778badac0d@postgresql-vm:~$

student-04-9c778badac0d@postgresql-vm:~$ ^C
student-04-9c778badac0d@postgresql-vm:~$ sudo nano /etc/postgresql/13/main/pg_hba.conf
student-04-9c778badac0d@postgresql-vm:~$ 
student-04-9c778badac0d@postgresql-vm:~$ sudo systemctl start postgresql@13-main
student-04-9c778badac0d@postgresql-vm:~$ 


$ gcloud sql connect postgresql-cloudsql --user=postgres --quiet
Allowlisting your IP for incoming connection for 5 minutes...done.     
Connecting to database with SQL user [postgres].Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

postgres=> \c orders;
Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "orders" as user "postgres".
orders=> select * from distribution_centers;
 longitude | latitude |                    name                     | id
-----------+----------+---------------------------------------------+----
 -89.9711  | 35.1174  | Memphis TN                                  |  1
 -87.6847  | 41.8369  | Chicago IL                                  |  2
 -95.3698  | 29.7604  | Houston TX                                  |  3
 -118.25   | 34.05    | Los Angeles CA                              |  4
 -90.0667  | 29.95    | New Orleans LA                              |  5
 -73.7834  | 40.634   | Port Authority of New York/New Jersey NY/NJ |  6
 -75.1667  | 39.95    | Philadelphia PA                             |  7
 -88.0431  | 30.6944  | Mobile AL                                   |  8
 -79.9333  | 32.7833  | Charleston SC                               |  9
 -81.1167  | 32.0167  | Savannah GA                                 | 10
(10 rows)

orders=> \q
$ export VM_NAME=postgresql-vm
$ export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
$ export POSTGRESQL_IP=$(gcloud compute instances describe ${VM_NAME} \
  --zone=us-east1-d --format="value(networkInterfaces[0].accessConfigs[0].natIP)")
$ echo $POSTGRESQL_IP
34.23.102.1
$ psql -h $POSTGRESQL_IP -p 5432 -d orders -U replication_admin
Password for user replication_admin:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.10 (Debian 13.10-1.pgdg100+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

orders=> \c orders;
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.10 (Debian 13.10-1.pgdg100+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "orders" as user "replication_admin".
orders=> insert into distribution_centers values(-80.1918,25.7617,'Miami FL',11);
INSERT 0 1
orders=> \q
$ gcloud sql connect postgresql-cloudsql --user=postgres --quiet
Allowlisting your IP for incoming connection for 5 minutes...done.     
Connecting to database with SQL user [postgres].Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

postgres=> \c orders;
Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "orders" as user "postgres".
orders=> select * from distribution_centers;
 longitude | latitude |                    name                     | id
-----------+----------+---------------------------------------------+----
 -89.9711  | 35.1174  | Memphis TN                                  |  1
 -87.6847  | 41.8369  | Chicago IL                                  |  2
 -95.3698  | 29.7604  | Houston TX                                  |  3
 -118.25   | 34.05    | Los Angeles CA                              |  4
 -90.0667  | 29.95    | New Orleans LA                              |  5
 -73.7834  | 40.634   | Port Authority of New York/New Jersey NY/NJ |  6
 -75.1667  | 39.95    | Philadelphia PA                             |  7
 -88.0431  | 30.6944  | Mobile AL                                   |  8
 -79.9333  | 32.7833  | Charleston SC                               |  9
 -81.1167  | 32.0167  | Savannah GA                                 | 10
 -80.1918  | 25.7617  | Miami FL                                    | 11
(11 rows)

orders=> \q
$$ gcloud sql connect postgresql-cloudsql --user=postgres --quiet
Allowlisting your IP for incoming connection for 5 minutes...done.     
Connecting to database with SQL user [postgres].Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

postgres=> \c orders;
Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "orders" as user "postgres".
orders=> select * from distribution_centers;
 longitude | latitude |                    name                     | id
-----------+----------+---------------------------------------------+----
 -89.9711  | 35.1174  | Memphis TN                                  |  1
 -87.6847  | 41.8369  | Chicago IL                                  |  2
 -95.3698  | 29.7604  | Houston TX                                  |  3
 -118.25   | 34.05    | Los Angeles CA                              |  4
 -90.0667  | 29.95    | New Orleans LA                              |  5
 -73.7834  | 40.634   | Port Authority of New York/New Jersey NY/NJ |  6
 -75.1667  | 39.95    | Philadelphia PA                             |  7
 -88.0431  | 30.6944  | Mobile AL                                   |  8
 -79.9333  | 32.7833  | Charleston SC                               |  9
 -81.1167  | 32.0167  | Savannah GA                                 | 10
(10 rows)

orders=> \q
$ export VM_NAME=postgresql-vm
$ export PROJECT_ID=$(gcloud config list --format 'value(core.project)')
$ export POSTGRESQL_IP=$(gcloud compute instances describe ${VM_NAME} \
  --zone=us-east1-d --format="value(networkInterfaces[0].accessConfigs[0].natIP)")
$ echo $POSTGRESQL_IP
34.23.102.1
$ psql -h $POSTGRESQL_IP -p 5432 -d orders -U replication_admin
Password for user replication_admin:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.10 (Debian 13.10-1.pgdg100+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

orders=> \c orders;
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.10 (Debian 13.10-1.pgdg100+1))
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "orders" as user "replication_admin".
orders=> insert into distribution_centers values(-80.1918,25.7617,'Miami FL',11);
INSERT 0 1
orders=> \q
$ gcloud sql connect postgresql-cloudsql --user=postgres --quiet
Allowlisting your IP for incoming connection for 5 minutes...done.     
Connecting to database with SQL user [postgres].Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
Type "help" for help.

postgres=> \c orders;
Password:
psql (15.2 (Debian 15.2-1.pgdg110+1), server 13.7)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, compression: off)
You are now connected to database "orders" as user "postgres".
orders=> select * from distribution_centers;
 longitude | latitude |                    name                     | id
-----------+----------+---------------------------------------------+----
 -89.9711  | 35.1174  | Memphis TN                                  |  1
 -87.6847  | 41.8369  | Chicago IL                                  |  2
 -95.3698  | 29.7604  | Houston TX                                  |  3
 -118.25   | 34.05    | Los Angeles CA                              |  4
 -90.0667  | 29.95    | New Orleans LA                              |  5
 -73.7834  | 40.634   | Port Authority of New York/New Jersey NY/NJ |  6
 -75.1667  | 39.95    | Philadelphia PA                             |  7
 -88.0431  | 30.6944  | Mobile AL                                   |  8
 -79.9333  | 32.7833  | Charleston SC                               |  9
 -81.1167  | 32.0167  | Savannah GA                                 | 10
 -80.1918  | 25.7617  | Miami FL                                    | 11
(11 rows)

orders=> \q
$
```