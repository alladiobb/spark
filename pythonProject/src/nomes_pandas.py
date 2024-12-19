from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("app") \
    .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
    .getOrCreate()

print("------------------------")
print(spark)
print("------------------------")

import pyspark.pandas as ps

# Read CSV using pandas-on-Spark
get_nomes = ps.read_csv("/home/alladio/Downloads/")  # Use a specific file name, not just a directory.

print(get_nomes)

# Display information about the DataFrame
get_nomes.info()
