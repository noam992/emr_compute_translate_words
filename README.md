# Datalake Translate Words using EMR compute

Welcome to the Datalake Translate Words project repository. This project utilizes AWS EMR (Elastic MapReduce) to efficiently lift heavy data, perform data extraction, transformation, and loading (ETL) tasks using Spark, and store the results in a curated directory in AWS S3. The data extraction is achieved through API calls to RapidAPI's Urban Dictionary.

## AWS EMR Overview

AWS EMR is a powerful service for processing large amounts of data using open-source tools such as Apache Spark and Apache Hadoop. It provides a scalable, secure, and cost-effective solution for processing and analyzing big data.

## Repository Structure

```
datalake-translate-words/
│
├── scripts/
│ ├── curated.py
│ ├── raw.py
│ └── config/
│ └── hadoop_config.sh
│
├── raw/
│ └── [word]/
│ ├── year=YYYY/
│ │ ├── month=MM/
│ │ │ └── day=dd/
│ │ │ └── [API_response].json
│ │ │
│ │ └── ...
│ │
│ └── ...
│
├── curated/
│ └── [word]/
│ ├── year=YYYY/
│ │ ├── month=MM/
│ │ │ └── day=dd/
│ │ │ └── [curated_data].parquet
│ │ │
│ │ └── ...
│ │
│ └── ...
│
└── spark-logs/
```

## Workflow Overview

1. **Data Extraction:**
   - A Lambda Function is triggered daily via CloudWatch Events.
   - The Lambda Function is responsible for initiating an AWS EMR cluster with the necessary configuration detailed in `LF_Trigger_Emr.py`.
   - The EMR cluster runs Spark jobs specified in `.PY` files, extracting data from the Urban Dictionary API.
   - Extracted JSON data is saved to S3 in partitioned folders based on the word and timestamp.

2. **Data Curating:**
   - The curated directory in S3 is computed using EMR and Spark.
   - The curated data is stored in Parquet files for fast access during data analysis.

3. **Data Analysis:**
   - Athena can be used to query the data stored in the curated directory due to its compatibility with the Parquet file format.

## Getting Started

1. Choose an API call for data extraction and configure it in `etl/extract/raw.py`. If using the provided example, register for a free API key at [RapidAPI Hub](https://rapidapi.com/hub) and use the [Urban Dictionary API](https://rapidapi.com/community/api/urban-dictionary/).

2. Create an S3 bucket named `datalake-translate-words` and organize it according to the structure mentioned above.

3. Upload the necessary scripts and configurations to the specified directories within the S3 bucket.

4. Create a Lambda Function and copy the content of `LF_Trigger_Emr.py` to it. This function will trigger the AWS EMR cluster with the required configuration.

5. Execute the Lambda Function to initiate the data extraction and curation process.

Feel free to explore and modify the code based on your specific requirements. For any questions or issues, please refer to the documentation or raise an issue in the repository. Happy data processing!

