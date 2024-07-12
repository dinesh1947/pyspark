from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("user_data").getOrCreate()

# Load dataset
file_path = "users.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the first few rows
df.show(5)
