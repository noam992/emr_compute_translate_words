import sys
import os
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession
from datetime import datetime

# windows configures
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

S3_DATA_INPUT_PATH = 's3://datalake-translate-words/raw'
S3_DATA_OUTPUT_PATH = 's3://datalake-translate-words/curated'

# S3 credentials
AWS_ACCESS_KEY_ID = '<>'
AWS_SECRET_ACCESS_KEY = '<>'
REGION = 'us-east-1'

# Create a SparkSession.
print("Creating SparkSession...")
spark = SparkSession.builder.appName('stg_word_translate') \
    .config('spark.hadoop.fs.s3a.access.key', AWS_ACCESS_KEY_ID) \
    .config('spark.hadoop.fs.s3a.secret.key', AWS_SECRET_ACCESS_KEY) \
    .getOrCreate()

def calculate():
    return True

if __name__ == "__main__":
    calculate()