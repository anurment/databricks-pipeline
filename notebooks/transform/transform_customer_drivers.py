# Databricks notebook source
from pyspark.sql.functions import col, current_timestamp, substring, expr, to_date
from pyspark.sql.types import StructType, StructField, StringType, BooleanType, TimestampType, DateType, DoubleType, IntegerType

# Define the schema for the silver table
schema = StructType(fields=[
    StructField("date", DateType(), False),
    StructField("customer_id", StringType(), False),
    StructField("monthly_salary", DoubleType(), True),
    StructField("health_score", IntegerType(), True),
    StructField("current_debt", DoubleType(), True),
    StructField("category", StringType(), True),
    StructField("processing_time", TimestampType(), True),
    StructField("is_risk_customer", BooleanType(), True)
    
])

# Load the bronze table
bronze_df = spark.table("bronze_catalog.customer_driver.bronze_customer_drivers")

# drop some columns
silver_df = bronze_df.drop('_rescued_data')
silver_df = silver_df.drop('source_file')



# fill some possible null values
silver_df = silver_df.fillna({'monthly_salary':0,
                            'health_score':100,
                            'current_debt': 0,
                            'category': 'OTHERS'})

silver_df = silver_df \
                .withColumnRenamed('customerId', 'customer_id') \
                .withColumn('is_risk_customer', col('health_score') < 100) \
                .withColumn('date', to_date(silver_df['date'], 'yyyy-MM-dd')) \
                .withColumn("processing_time", current_timestamp()) \
                .withColumn("monthly_salary", col("monthly_salary").cast("double")) \
                .withColumn("current_debt", col("current_debt").cast("double")) \
                .withColumn("health_score", col("health_score").cast("int"))

# Apply the schema to the dataframe
silver_df = spark.createDataFrame(silver_df.rdd, schema=schema)

# Save the silver table
silver_df.write.format("delta").mode("overwrite").partitionBy('date').saveAsTable("silver_catalog.customer_driver.silver_customer_drivers")
