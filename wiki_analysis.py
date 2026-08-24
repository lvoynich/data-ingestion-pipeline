from pyspark.sql import SparkSession

# 1. Initialize local Spark Engine
spark = SparkSession.builder \
    .appName("WikipediaClickstreamAnalysis") \
    .getOrCreate()

# 2. Load the local CSV dataset
file_path = "./wiki_data/wiki_clickstream.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# 3. Print Schema (Matches Codecademy Step 1)
print("\n--- DATASET SCHEMA ---")
df.printSchema()

# 4. Register as a Virtual Database Table for SQL Queries
df.createOrReplaceTempView("clickstream")

# 5. Execute SQL Query: Find top traffic sources to "Apache_Spark"
print("\n--- TOP TRAFFIC SOURCES TO APACHE_SPARK ---")
spark.sql("""
    SELECT referrer, SUM(count) as total_clicks
    FROM clickstream
    WHERE resource = 'Apache_Spark'
    GROUP BY referrer
    ORDER BY total_clicks DESC
    LIMIT 5
""").show()

# 6. Safely shut down Spark engine
spark.stop()
