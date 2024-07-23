#!/bin/bash
gcloud dataproc jobs submit pyspark \
       --cluster sparktodp \
       --region us-central1 \
       spark_analysis.py \
       -- --bucket=$1
