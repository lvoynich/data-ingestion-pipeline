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

# 5. EXECUTE ADVANCED SQL QUERIES

# QUERY A: Find the Top 5 Most Visited Articles on Wikipedia overall
print("\n=== TOP 5 MOST VISITED ARTICLES OVERALL ===")
spark.sql("""
    SELECT resource as article_name, SUM(count) as total_views
    FROM clickstream
    GROUP BY resource
    ORDER BY total_views DESC
    LIMIT 5
""").show()

# QUERY B: Find Top 5 Internal Search Results (Referred by "Special:Search")
# This shows what people are actively looking up to land on articles
print("\n=== TOP 5 ARTICLES FOUND VIA INTERNAL SEARCH ===")
spark.sql("""
    SELECT resource as searched_article, SUM(count) as search_clicks
    FROM clickstream
    WHERE referrer = 'Special:Search'
    GROUP BY resource
    ORDER BY search_clicks DESC
    LIMIT 5
""").show()

# QUERY C: Find Top 5 External Traffic Referrers (Excluding internal wiki clicks)
# Proves you can handle negative filtering logic (NOT LIKE / NOT IN)
print("\n=== TOP 5 EXTERNAL TRAFFIC DRIVERS ===")
spark.sql("""
    SELECT referrer, SUM(count) as external_clicks
    FROM clickstream
    WHERE referrer NOT IN ('Main_Page', 'Special:Search', 'Wikipedia') 
      AND referrer NOT LIKE '%_page%'
    GROUP BY referrer
    ORDER BY external_clicks DESC
    LIMIT 5
""").show()

# 6. Safely shut down Spark engine
spark.stop()

