#import libraries and init spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
print
#load data
# df_device = spark.read.json("/")