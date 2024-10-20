# Databricks notebook source
# Import functions
from pyspark.sql.functions import col, current_timestamp
from  delta.tables import *

# COMMAND ----------

#  external_location_path from ../includes/configurations.py
# %run commands need to be in separate cells

# COMMAND ----------

# MAGIC %run "../includes/configurations.py"

# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.types import StructType, StructField, StringType, BooleanType

date = '2022-09-11'

# Define variables used in code below
file_path = f"{external_location_path}customer"  # from ../includes/configurations.py
username = spark.sql("SELECT regexp_replace(current_user(), '[^a-zA-Z0-9]', '_')").first()[0]
table_name = "bronze_catalog.customer.bronze_customer"
checkpoint_path = f"/tmp/{username}/_checkpoint/customer_loader"

# Configure Auto Loader to ingest csv data to a Delta table with UPSERT technique
# Remember to first initialize the bronze_customer table and schema
def upsertToDelta(microBatchOutputDF, batchId):
    deltaTable = DeltaTable.forName(spark, table_name)
    microBatchOutputDF.createOrReplaceTempView("staged_updates")
    deltaTable.alias("t").merge(
        source=microBatchOutputDF.alias("s"),
        condition="t.customerId = s.customerId"
    ).whenMatchedUpdate(set={
        "customerId": "s.customerId",
        "firstName": "s.firstName",
        "lastName": "s.lastName",
        "phone": "s.phone",
        "email": "s.email",
        "gender": "s.gender",
        "address": "s.address",
        "is_active": "s.is_active",
        "processing_time": current_timestamp()  # Ensure processing_time is updated
    }).whenNotMatchedInsert(values={
        "customerId": "s.customerId",
        "firstName": "s.firstName",
        "lastName": "s.lastName",
        "phone": "s.phone",
        "email": "s.email",
        "gender": "s.gender",
        "address": "s.address",
        "is_active": "s.is_active",
        "processing_time": current_timestamp()  # Ensure processing_time is inserted
    }).execute()

streaming_df = (spark.readStream
                .format("cloudFiles")
                .option("cloudFiles.format", "csv")
                .option("cloudFiles.schemaLocation", checkpoint_path)
                .load(file_path)
                .dropDuplicates(["customerId"])
                .select("*", 
                        col("_metadata.file_path").alias("source_file"),
                        current_timestamp().alias("processing_time")))
                

query = (streaming_df.writeStream
         .format("delta")
         .outputMode("update")
         .option("checkpointLocation", checkpoint_path)
         .foreachBatch(upsertToDelta)
         .trigger(availableNow=True)
         .start(table_name))
