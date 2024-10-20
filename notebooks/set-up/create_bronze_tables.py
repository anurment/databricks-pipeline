# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, TimestampType

# COMMAND ----------

# initialize bronze_customer table
customer_table_name = "bronze_catalog.customer.bronze_customer"

customer_schema = StructType([
    StructField("customerId", StringType(), False),
    StructField("firstName", StringType(), False),
    StructField("lastName", StringType(), False),
    StructField("phone", StringType(), True),
    StructField("email", StringType(), True),
    StructField("gender", StringType(), True),
    StructField("address", StringType(), True),
    StructField("is_active", StringType(), True),
    StructField("processing_time", TimestampType(), True)

])

spark.createDataFrame([], customer_schema).write.format("delta").saveAsTable(customer_table_name)

# COMMAND ----------

# initialize bronze_customer_drivers table
customer_driver_table_name = "bronze_catalog.customer_driver.bronze_customer_drivers"

customer_driver_schema = StructType(fields=[
    StructField("date", StringType(), False),
    StructField("customerId", StringType(), False),
    StructField("monthly_salary", StringType(), True),
    StructField("health_score", StringType(), True),
    StructField("current_debt", StringType(), True),
    StructField("category", StringType(), True),
    StructField("processing_time", TimestampType(), True)
])

spark.createDataFrame([], customer_driver_schema).write.format("delta").saveAsTable(customer_driver_table_name)

# COMMAND ----------

# initialize bronze_loan_trx table
loan_trx_table_name = "bronze_catalog.loan_trx.bronze_loan_trx"

loan_trx_schema = StructType(fields=[
    StructField("date", StringType(), False),
    StructField("customerId", StringType(), False),
    StructField("paymentPeriod", StringType(), False),
    StructField("loanAmount", StringType(), False),
    StructField("currencyType", StringType(), False),
    StructField("evaluationChannel", StringType(), False),
    StructField("interest_rate", StringType(), False),
    StructField("processing_time", TimestampType(), True)
])

spark.createDataFrame([], loan_trx_schema).write.format("delta").saveAsTable(loan_trx_table_name)

