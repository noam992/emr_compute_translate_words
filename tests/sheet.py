import sys
import os
from typing import List
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

print(sys.executable)
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

AWS_ACCESS_KEY_ID = '<insert access key>'
AWS_SECRET_ACCESS_KEY = '<insert secret key>'
REGION = 'us-east-1'

print(os.environ['PYSPARK_PYTHON'])

if __name__ == "__main__":

    print("Creating SparkSession...")
    spark = SparkSession.builder.appName('stg_word_translate') \
        .config('spark.hadoop.fs.s3a.access.key', AWS_ACCESS_KEY_ID) \
        .config('spark.hadoop.fs.s3a.secret.key', AWS_SECRET_ACCESS_KEY) \
        .getOrCreate()