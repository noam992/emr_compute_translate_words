# Datalake Translate Words using EMR compute

Welcome to the Datalake Translate Words project repository. This project utilizes AWS EMR (Elastic MapReduce) to efficiently lift heavy data, perform data extraction, transformation, and loading (ETL) tasks using Spark, and store the results in a curated directory in AWS S3. The data extraction is achieved through API calls to RapidAPI's Urban Dictionary.

## AWS EMR Overview

AWS EMR is a powerful service for processing large amounts of data using open-source tools such as Apache Spark and Apache Hadoop. It provides a scalable, secure, and cost-effective solution for processing and analyzing big data.

## Repository Structure


User
Write a README file for github repo project using the points:
* One of the powerful service to lift heavy data and transfer it is EMR
* AWS EMR is ..
* the repo contains building of datalake that use spark in order to extract and transfer data (see the PNG file and the red sign, AWS EMR Architucture.png).
* as you can see the process start from Lamnda Function which applyed once a day thank for CloudWatch Event and the Lambda Function contains the details and the hardware for AWS EMR and the steps (.PY files) that will run on the EMR
* the extraction for our case to dimostarct the process I used https://rapidapi.com/hub and chosed to extract using API call tranclation of words.
* so the first process where the data start, source to target, is extract data from the api call when I send a word and getting 10 optinal translation of that word, then the json are saved in s3 as json file in partition folding of <word>/year=YYYY/month=MM/day=dd.
* the partition folding use for athena to be able to read the data
* Athena is a service for ..
*  the next step of the process is curated directory in AWS s3 where I calculate and use EMR to compute the json file in parallal and disturbuted method, SPARK.
in curated directory the files are saved in Parquet file to get access fest when uses want to analys the data.

In order to use the code please choose the API call that you will use in etl/extract/raws.py. if you would like to use the same one I used so register to https://rapidapi.com/hub web and use https://rapidapi.com/community/api/urban-dictionary/ free API call.
in addtion use the following structure to build your datalake in AWS S3 and upload the files in the right places.

here pleace draw a structure:
s3 bucket name: datalake-translate-words
under it: scripts, raw,curated, spark-logs.
inside scripts upload: curated.py, raw.py and create subdirectory with file config/hadoop_config.sh

create Lambda Function and copy content of file LF_Trigger_Emr.py. that function will invoke and create AWS EMR with all the steps (running bootstramp action for additional python libraries and running raw.py then curated.py files)
ChatGPT
Datalake Translate Words
Welcome to the Datalake Translate Words project repository. This project utilizes AWS EMR (Elastic MapReduce) to efficiently lift heavy data, perform data extraction, transformation, and loading (ETL) tasks using Spark, and store the results in a curated directory in AWS S3. The data extraction is achieved through API calls to RapidAPI's Urban Dictionary.

AWS EMR Overview
AWS EMR is a powerful service for processing large amounts of data using open-source tools such as Apache Spark and Apache Hadoop. It provides a scalable, secure, and cost-effective solution for processing and analyzing big data.

Repository Structure
css
Copy code
datalake-translate-words/
│
├── scripts/
│   ├── curated.py
│   ├── raw.py
│   └── config/
│       └── hadoop_config.sh
│
├── raw/
│   └── [word]/
│       ├── year=YYYY/
│       │   ├── month=MM/
│       │   │   └── day=dd/
│       │   │       └── [API_response].json
│       │   │
│       │   └── ...
│       │
│       └── ...
│
├── curated/
│   └── [word]/
│       ├── year=YYYY/
│       │   ├── month=MM/
│       │   │   └── day=dd/
│       │   │       └── [curated_data].parquet
│       │   │
│       │   └── ...
│       │
│       └── ...
│
└── spark-logs/
Workflow Overview
Data Extraction:

A Lambda Function is triggered daily via CloudWatch Events.
The Lambda Function is responsible for initiating an AWS EMR cluster with the necessary configuration detailed in LF_Trigger_Emr.py.
The EMR cluster runs Spark jobs specified in .PY files, extracting data from the Urban Dictionary API.
Extracted JSON data is saved to S3 in partitioned folders based on the word and timestamp.
Data Curating:

The curated directory in S3 is computed using EMR and Spark.
The curated data is stored in Parquet files for fast access during data analysis.
Data Analysis:

Athena can be used to query the data stored in the curated directory due to its compatibility with the Parquet file format.
Getting Started
Choose an API call for data extraction and configure it in etl/extract/raw.py. If using the provided example, register for a free API key at RapidAPI Hub and use the Urban Dictionary API.

Create an S3 bucket named datalake-translate-words and organize it according to the structure mentioned above.

Upload the necessary scripts and configurations to the specified directories within the S3 bucket.

Create a Lambda Function and copy the content of LF_Trigger_Emr.py to it. This function will trigger the AWS EMR cluster with the required configuration.

Execute the Lambda Function to initiate the data extraction and curation process.

Feel free to explore and modify the code based on your specific requirements. For any questions or issues, please refer to the documentation or raise an issue in the repository. Happy data processing!

User
can you write your answer in .rm format that I can copy and paste in README.rm file ?
ChatGPT
Certainly! Here is the content in a Markdown (.md) format that you can copy and paste into your README.md file:

markdown
Copy code
# Datalake Translate Words

Welcome to the Datalake Translate Words project repository. This project utilizes AWS EMR (Elastic MapReduce) to efficiently lift heavy data, perform data extraction, transformation, and loading (ETL) tasks using Spark, and store the results in a curated directory in AWS S3. The data extraction is achieved through API calls to RapidAPI's Urban Dictionary.

## AWS EMR Overview

AWS EMR is a powerful service for processing large amounts of data using open-source tools such as Apache Spark and Apache Hadoop. It provides a scalable, secure, and cost-effective solution for processing and analyzing big data.

## Repository Structure

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
│ └── insights/
│ ├── year=YYYY/
│   ├── month=MM/
│     └── day=dd/
│     └── [curated_data].parquet
│
└── spark-logs/


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
