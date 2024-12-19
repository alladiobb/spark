#import libraries and init spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()

# spark.sql("""
#     CREATE TEMPORARY VIEW nomes
#     USING org.apache.spark.sql.csv
#     OPTIONS (path "/home/alladio/Downloads/*.csv")
# """)


# Read all CSV files in the specified directory
df = (((spark.read.format("csv")
      .option("header", "true"))
      .option("inferSchema", "true"))
      .load("/home/alladio/Downloads/*.csv"))

# Create a temporary view
df.createOrReplaceTempView("nomes")


print(spark.catalog.listTables())

spark.sql("SELECT * FROM nomes LIMIT 10").show()

