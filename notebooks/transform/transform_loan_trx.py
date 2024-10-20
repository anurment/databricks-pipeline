# Databricks notebook source
from pyspark.sql.functions import col, current_timestamp, substring, expr, to_date
from pyspark.sql.types import StructType, StructField, StringType, BooleanType, TimestampType, DateType, DoubleType, IntegerType

# Define the schema for the silver table
schema = StructType(fields=[
    StructField("date", DateType(), False),
    StructField("customer_id", StringType(), False),
    StructField("payment_period", IntegerType(), False),
    StructField("loan_amount", DoubleType(), False),
    StructField("currency_type", StringType(), False),
    StructField("evaluation_channel", StringType(), False),
    StructField("interest_rate", DoubleType(), False),
    StructField("processing_time", TimestampType(), True),
    
])

# Load the bronze table
bronze_df = spark.table("bronze_catalog.loan_trx.bronze_loan_trx")

# drop some columns
silver_df = bronze_df.drop('_rescued_data')
silver_df = silver_df.drop('source_file')


#renaming and retyping
silver_df = silver_df \
                .withColumnRenamed("customerId", "customer_id") \
                .withColumnRenamed('paymentPeriod' , 'payment_period') \
                .withColumnRenamed('loanAmount' , 'loan_amount') \
                .withColumnRenamed('currencyType' , 'currency_type') \
                .withColumnRenamed('evaluationChannel' , 'evaluation_channel') \
                .withColumn('date', to_date(silver_df['date'], 'dd/MM/yyyy')) \
                .withColumn("payment_period", col("payment_period").cast("int")) \
                .withColumn("loan_amount", col("loan_amount").cast("double")) \
                .withColumn("interest_rate", col("interest_rate").cast("double")) \


# Apply the schema to the dataframe
silver_df = spark.createDataFrame(silver_df.rdd, schema=schema)

# Save the silver table
silver_df.write.format("delta").mode("overwrite").partitionBy('date').saveAsTable("silver_catalog.loan_trx.silver_loan_trx")
