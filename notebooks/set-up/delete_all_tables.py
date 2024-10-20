# Databricks notebook source
# Drop all the tables

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS bronze_catalog.customer.bronze_customer;
# MAGIC DROP TABLE IF EXISTS bronze_catalog.customer_driver.bronze_customer_drivers;
# MAGIC DROP TABLE IF EXISTS bronze_catalog.loan_trx.bronze_loan_trx;
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS silver_catalog.customer.silver_customer;
# MAGIC DROP TABLE IF EXISTS silver_catalog.customer_driver.silver_customer_drivers;
# MAGIC DROP TABLE IF EXISTS silver_catalog.loan_trx.silver_loan_trx;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS gold_catalog.customer.gold_customer;
# MAGIC DROP TABLE IF EXISTS gold_catalog.loan_trx.silver_loan_trx;

# COMMAND ----------

# Delete the checkpoints for autoloader

username = spark.sql("SELECT regexp_replace(current_user(), '[^a-zA-Z0-9]', '_')").first()[0]

checkpoint_path = f"/tmp/{username}/_checkpoint/customer_loader"
dbutils.fs.rm(checkpoint_path, True)

checkpoint_path = f"/tmp/{username}/_checkpoint/customer_driver_loader"
dbutils.fs.rm(checkpoint_path, True)

checkpoint_path = f"/tmp/{username}/_checkpoint/loan_trx_loader"
dbutils.fs.rm(checkpoint_path, True)
