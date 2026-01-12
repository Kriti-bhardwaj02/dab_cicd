# Databricks notebook source
df = spark.range(10)
display(df)


#this is range func

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from `test-neha-catalog`.bronze.claim_bronze
