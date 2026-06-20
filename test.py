# test_spark.py

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Test") \
    .getOrCreate()

print("Spark Started Successfully")

spark.stop()