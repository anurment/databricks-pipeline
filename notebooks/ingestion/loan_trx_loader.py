# Databricks notebook source
# Import functions
from pyspark.sql.functions import col, current_timestamp

# COMMAND ----------

#  external_location_path from ../includes/configurations.py
# %run commands need to be in separate cells

# COMMAND ----------

# MAGIC %run "../includes/configurations.py"

# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, BooleanType

# Define variables used in code below
file_path = f"{external_location_path}transactions"  # from ../includes/configurations.py
username = spark.sql("SELECT regexp_replace(current_user(), '[^a-zA-Z0-9]', '_')").first()[0]
table_name = "bronze_catalog.loan_trx.bronze_loan_trx"
checkpoint_path = f"/tmp/{username}/_checkpoint/loan_trx_loader"

# Configure Auto Loader to ingest csv data to a Delta table with normal append technique
# Remember to first initialize the bronze_customer table and schema
(spark.readStream
  .format("cloudFiles")
  .option("cloudFiles.format", "csv")
  .option("cloudFiles.schemaLocation", checkpoint_path)
  .load(file_path)
  .select("*", col("_metadata.file_path").alias("source_file"), current_timestamp().alias("processing_time"))
  .writeStream
  .option("checkpointLocation", checkpoint_path)
  .trigger(availableNow=True)
  .option("mergeSchema", "true")
  .toTable(table_name))
