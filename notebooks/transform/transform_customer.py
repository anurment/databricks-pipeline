# Databricks notebook source
from pyspark.sql.functions import col, current_timestamp, substring, expr
from pyspark.sql.types import StructType, StructField, StringType, BooleanType, TimestampType

# Define the schema for the silver table
schema = StructType(fields=[
    StructField("customer_id", StringType(), False),
    StructField("first_name", StringType(), False),
    StructField("last_name", StringType(), False),
    StructField("phone", StringType(), True),
    StructField("email", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("address", StringType(), True),
    StructField("is_active", BooleanType(), True),
    StructField("processing_time", TimestampType(), True)
])

# Load the bronze table
bronze_df = spark.table("bronze_catalog.customer.bronze_customer")

# Transform and rename columns
silver_df = bronze_df.withColumnRenamed("customerId", "customer_id") \
    .withColumnRenamed("firstName", "first_name") \
    .withColumnRenamed("lastName", "last_name") \
    .withColumn("processing_time", current_timestamp()) \
    .withColumn('gender', substring('gender', 1,1)) \
    .withColumn("is_active", expr("is_active == 'TRUE'"))

# Apply the schema to the dataframe
silver_df = spark.createDataFrame(silver_df.rdd, schema=schema)

# Save the silver table
silver_df.write.format("delta").mode("overwrite").saveAsTable("silver_catalog.customer.silver_customer")
