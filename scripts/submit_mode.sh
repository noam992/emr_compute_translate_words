#!/bin/bash
# on local machine for debugging (on windows using powershell adding conf (to replacing python3 with python))
spark-submit --master local[*] --deploy-mode client --conf "spark.pyspark.python=python" etl/extract/stg_extract_dictionary.py home

# on EMR cluster for debugging
spark-submit --master yarn --deploy-mode cluster etl/extract/stg_extract_dictionary.py