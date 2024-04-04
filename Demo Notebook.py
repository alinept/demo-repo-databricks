# Databricks notebook source
# MAGIC %fs ls '/databricks-datasets'

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()


# COMMAND ----------

dbutils.fs.ls('/databricks-datasets/')

# COMMAND ----------

files = dbutils.fs.ls('/databricks-datasets/')
display(files)

# COMMAND ----------


