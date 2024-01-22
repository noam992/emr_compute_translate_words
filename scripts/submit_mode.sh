#!/bin/bash
# on local machine for debugging
Set-Alias -Name python3 -Value python
spark-submit --deploy-mode client --master local[*] etl/extract/stg_extract_dictionary.py
# running spark on windows using powershell adding conf (replacing python3 with python)
spark-submit --conf "spark.pyspark.python=python" etl/extract/stg_extract_dictionary.py home

spark-submit \
  --master <master-url> \
  --deploy-mode <deploy-mode> \
  --conf <key<=<value> \
  --driver-memory <value>g \
  --executor-memory <value>g \
  --executor-cores <number of cores>  \
  --py-files file1.py,file2.py,file3.zip, file4.egg \

# on EMR cluster for debugging
spark-submit --deploy-mode cluster --master yarn etl/extract/stg_extract_dictionary.py