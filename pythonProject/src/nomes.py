#import libraries and init spark session
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
# spark.conf.set("spark.sql.debug.maxToStringFields", "1000")  # Ajuste o valor conforme necessário
# print("----------------------------")
# print(spark)
# print("----------------------------")

# Passo 1: Ler os dados (JSON ou CSV)
df_device_raw = (spark.read
                 .option("multiline", "true")
                 .option("header", "true")
                 .csv("/home/alladio/Downloads/nomes.csv"))  # Exemplo com JSON

# Ou se for CSV
# df_device_raw = spark.read.option("header", "true").csv("/home/alladio/Downloads/dados.csv")

# Passo 2: Salvar os dados em formato Parquet
df_device_raw.write.mode("overwrite").parquet("/home/alladio/Downloads/parquet/")

# Passo 3: Recarregar os dados Parquet para aplicar transformações ou filtros
df_device_parquet = spark.read.option("mode", "PERMISSIVE").parquet("/home/alladio/Downloads/parquet/")
# df_device_parquet.repartition(1)

# Agora você pode realizar filtros ou transformações
# print("----------------------------")
# print(df_device_parquet.count())
# print("----------------------------")

# df_device_parquet.select("alternative_names","first_name","frequency_female","frequency_male")
# df_device_parquet.select("alternative_names")
# df_device_parquet.selectExpr("first_name")
df_device_parquet.filter(df_device_parquet.first_name == "ALADIO").show(truncate=False)
# df_device_parquet.show()
