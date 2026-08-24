import os
import csv
import random

output_dir = os.path.expanduser("~/Desktop/data-ingestion-pipeline/wiki_data")
os.makedirs(output_dir, exist_ok=True)
file_path = os.path.join(output_dir, "wiki_clickstream.csv")

pages = ["Main_Page", "Apache_Spark", "Python_(programming_language)", "Data_engineering", "Database", "Oracle_Database", "Wikipedia", "Special:Search"]
referrers = ["google", "bing", "twitter", "other-wikipedia", "direct"] + pages

with open(file_path, mode="w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["referrer", "resource", "count"]) # Headers
    for _ in range(10000):
        ref = random.choice(referrers)
        res = random.choice(pages)
        if ref != res: # Skip clicking to the exact same page
            writer.writerow([ref, res, random.randint(10, 5000)])

print(f"Success! Generated 10,000 mock clickstream rows at: {file_path}")
