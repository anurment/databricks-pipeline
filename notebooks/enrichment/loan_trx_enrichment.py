# Databricks notebook source
from pyspark.sql.functions import *

customer_drivers_df = spark.table("silver_catalog.customer_driver.silver_customer_drivers")

loan_trx_df = spark.table("silver_catalog.loan_trx.silver_loan_trx")

# We join our two dataframes loan and customerDrivers to enrich our transactional data
featureLoanTrx_df = loan_trx_df.alias('l') \
                        .join(customer_drivers_df.alias('c'), 
                             (col('l.customer_id') == col('c.customer_id')) 
                             & (col('l.date') == col('c.date')), 
                             "inner") \
                        .select(col('l.date'),
                                col('l.customer_id'),
                                col('l.payment_period'),
                                col('l.loan_amount'),
                                col('l.currency_type'),
                                col('l.evaluation_channel'),
                                col('l.interest_rate'),
                                col('c.monthly_salary'),
                                col('c.health_score'),
                                col('c.current_debt'),
                                col('c.category'),
                                col('c.is_risk_customer'))

#Add timestamp                
featureLoanTrx_df = featureLoanTrx_df.withColumn("processing_time", current_timestamp())

#Save the table
featureLoanTrx_df.write.format("delta").mode("overwrite").partitionBy('date').saveAsTable("gold_catalog.loan_trx.feature_loan_trx")

# We are going to do some aggregations from our feature dataframe
aggLoanTrx_df = featureLoanTrx_df.groupBy('date',
                                       'payment_period',
                                       'currency_type',
                                       'evaluation_channel',
                                       'category') \
                              .agg(
                                sum('loan_amount').alias('sum_loan_amount'),
                                avg('loan_amount').alias('avg_loan_amount'),
                                sum('current_debt').alias('sum_current_debt'),
                                avg('interest_rate').alias('avg_interest_rate'),
                                max('interest_rate').alias('max_interest_rate'),
                                min('interest_rate').alias('min_interest_rate'),
                                avg('health_score').alias('avg_score'),
                                avg('monthly_salary').alias('avg_monthly_salary')) \
                              .orderBy('date', 'payment_period', 'evaluation_channel', 'category', 'currency_type')

#Add timestamp
aggLoanTrx_df = aggLoanTrx_df.withColumn("processing_time", current_timestamp())

#Save table
aggLoanTrx_df.write.format("delta").mode("overwrite").partitionBy('date').saveAsTable("gold_catalog.loan_trx.aggLoanTrx_df")
