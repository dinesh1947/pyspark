from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("HousePricePrediction").getOrCreate()

# Load dataset
file_path = "ames_housing.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the first few rows
# df.show(5)
df.describe().show()