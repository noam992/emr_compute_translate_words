import requests
import sys
import os
from typing import List
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

# windows configures
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

S3_DATA_OUTPUT_PATH = 's3://datalake-stock/silver/output.parquet'

# S3 credentials
AWS_ACCESS_KEY_ID = '<insert access key>'
AWS_SECRET_ACCESS_KEY = '<insert secret key>'
REGION = 'us-east-1'


def get_translating(word: str) -> List[dict]:

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term": word}

    headers = {
        "X-RapidAPI-Key": "fc30ecd86cmsh7f3cf76dfa6a129p133c0ejsn8f267f9f96b0",
        "X-RapidAPI-Host": "mashape-community-urban-dictionary.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    res_json = response.json()

    return res_json['list']

    # for key, value in res_json['list'][0].items():
    #     print(key, ': ', value)

def extract_an_item_from_list(lst: List[dict], item_num: int) -> dict:
    return lst[item_num]

def upload_to_s3(item):

    print("Writing processed data to S3...")
    item.write.mode('overwrite').parquet(S3_DATA_OUTPUT_PATH)

def main():
    word = sys.argv[1]
    print('The word is: ', word)
    print("Creating SparkSession...")

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
    translate_df.show()

if __name__ == "__main__":
    # Create a SparkSession
    print("Creating SparkSession...")
    spark = SparkSession.builder.appName('stg_word_translate') \
        .getOrCreate()
    
    main()