```bash
$ bq --location=EU mk --dataset movies
Dataset 'clear-router-f1f5fd34806b:movies' successfully created.

$  bq load --source_format=CSV \
 --location=EU \
 --autodetect movies.movielens_ratings \
 gs://dataeng-movielens/ratings.csv
Waiting on bqjob_r16099a61c6288c70_0000018b2d3d73a6_1 ... (23s) Current status: DONE 

$  bq load --source_format=CSV \
 --location=EU   \
 --autodetect movies.movielens_movies_raw \
 gs://dataeng-movielens/movies.csv
Waiting on bqjob_r5e7ea2f41a784b04_0000018b2d3deddd_1 ... (1s) Current status: DONE   


```