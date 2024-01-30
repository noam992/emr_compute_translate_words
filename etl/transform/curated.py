import sys
import os
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, max, min
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
spark = SparkSession.builder.appName('curated_word_translate') \
    .getOrCreate()

def get_current_date_components():
    # Get the current date and time
    current_date = datetime.now()

    # Extract year, month, and day components
    year = current_date.year
    month = current_date.month
    day = current_date.day

    return year, month, day

def get_s3_word_data() -> DataFrame:

    S3_PATH_INPUT = "{}/*/*/*/*".format(S3_DATA_INPUT_PATH)
    print("The path is: ", S3_PATH_INPUT)
    data = spark.read.json(S3_PATH_INPUT)

    print("lenght rows: ", data.count())
    print("data type: ", type(data))
    data.show()
    return data

def get_max_thumbs_up(df):
    result = df.groupBy("word") \
        .agg(max("thumbs_up").alias("max_thumbs_up"), \
            min("thumbs_up").alias("min_thumbs_up")
        )
    
    print("lenght rows: ", result.count())
    print("data type: ", type(result))
    result.show()
    return result

def upload_to_s3(spark_df):

    year, month, day = get_current_date_components()
    S3_PATH = "{}/insights/year={}/month={}/day={}".format(S3_DATA_OUTPUT_PATH, year, month, day)
    print("saved path: ", S3_PATH)
    
    print("Writing processed data to S3...")
    spark_df.write.parquet(S3_PATH, mode='overwrite')

if __name__ == "__main__":
    translate_df = get_s3_word_data()
    agg_thumbs_up = get_max_thumbs_up(translate_df)

    upload_to_s3(agg_thumbs_up)