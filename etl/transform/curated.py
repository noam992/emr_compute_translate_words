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
REGION = 'us-east-1'

# Create a SparkSession.
print("Creating SparkSession...")
spark = SparkSession.builder.appName('stg_word_translate') \
    .getOrCreate()

def get_s3_word_data():

    S3_PATH_INPUT = "{}/*/*/*/*".format(S3_DATA_INPUT_PATH)
    print("The path is: ", S3_PATH_INPUT)
    data = spark.read.json(S3_PATH_INPUT)
    data.show()

def calculate():
    return True

if __name__ == "__main__":
    get_s3_word_data()