import requests
import sys
import os
from typing import List
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession
from datetime import datetime

# windows configures
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

S3_DATA_OUTPUT_PATH = 's3://datalake-translate-words/raw'

# S3 credentials
REGION = 'us-east-1'

# Create a SparkSession.
print("Creating SparkSession...")
spark = SparkSession.builder.appName('raw_word_translate') \
    .getOrCreate()

def get_current_date_components():
    # Get the current date and time
    current_date = datetime.now()

    # Extract year, month, and day components
    year = current_date.year
    month = current_date.month
    day = current_date.day

    return year, month, day

def get_translating(word: str) -> List[dict]:

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term": word}

    headers = {
        "X-RapidAPI-Key": "insert your user key of rapidapi.com",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    res_json = response.json()

    return res_json['list']

def extract_an_item_from_list(lst: List[dict], item_num: int) -> dict:
    return lst[item_num]

def upload_to_s3(spark_df, word):

    year, month, day = get_current_date_components()
    S3_PATH = "{}/{}/year={}/month={}/day={}".format(S3_DATA_OUTPUT_PATH, word, year, month, day)
    print("saved path: ", S3_PATH)
    
    print("Writing processed data to S3...")
    spark_df.write.json(S3_PATH, mode='overwrite')
    # spark_df.write.parquet(S3_PATH, mode='overwrite')

def translate_word_fnc():
    word = sys.argv[1]
    print('The word is: ', word)

    translate_dict = get_translating(word)
    
    translate_item = extract_an_item_from_list(translate_dict, 0)
    print("Example of first translate word: ")
    print(translate_item)

    # Create a PySpark RDD (Resilient Distributed Dataset)
    translate_rdd = spark.sparkContext.parallelize(translate_dict)

    # # Define the schema for the Data Frame
    translate_schema = StructType([
        StructField("definition", StringType(), nullable=False),
        StructField("permalink", StringType(), nullable=False),
        StructField("thumbs_up", IntegerType(), nullable=False),
        StructField("author", StringType(), nullable=False),
        StructField("word", StringType(), nullable=False),
        StructField("defid", IntegerType(), nullable=False),
        StructField("current_vote", StringType(), nullable=False),
        StructField("written_on", StringType(), nullable=False),
        StructField("example", StringType(), nullable=False),
        StructField("thumbs_down", IntegerType(), nullable=False)
    ])

    # Apply the schema to the RDD and create a Data Frame
    translate_df = spark.createDataFrame(translate_rdd, translate_schema)

    # Print data frame
    print("Spark Dataframe: ")
    translate_df.show()

    upload_to_s3(translate_df, word)


if __name__ == "__main__":
    
    translate_word_fnc()