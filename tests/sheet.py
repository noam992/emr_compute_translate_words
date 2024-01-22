import sys
import os
from typing import List
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

print(sys.executable)
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

print(os.environ['PYSPARK_PYTHON'])

if __name__ == "__main__":

    print("Creating SparkSession...")
    spark = SparkSession.builder.appName('stg_word_translate') \
        .getOrCreate()