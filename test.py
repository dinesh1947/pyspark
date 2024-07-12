from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("PySpark_dc").getOrCreate() 
spark
df = spark.read.csv("users.csv",header = True, inferSchema = True)
df.show(4)
