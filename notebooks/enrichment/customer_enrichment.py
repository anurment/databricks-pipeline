# Databricks notebook source
from pyspark.sql.functions import current_timestamp

# Load the silver table
silver_df = spark.table("silver_catalog.customer.silver_customer")

gold_df = silver_df.select('customer_id',
                             'first_name',
                             'last_name',
                             'phone',
                             'email',
                             'gender',
                             'is_active')


gold_df = silver_df.withColumn("processing_time", current_timestamp())
gold_df.write.format("delta").mode("overwrite").saveAsTable("gold_catalog.customer.gold_customer")






