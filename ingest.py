import os
import random
from datetime import datetime
import json

# 1. Configuration
OUTPUT_DIR = os.path.expanduser("~/Desktop/data-ingestion-pipeline/raw_data")
os.makedirs(OUTPUT_DIR, exist_ok=True)

try:
    print(f"[{datetime.now()}] Generating local mock sensor data...")
    
    # 2. Create structured mock data simulating an internet connected sensor
    mock_data = {
        "metadata": {
            "sensor_id": "NYC-DATA-ENG-001",
            "timestamp": datetime.utcnow().isoformat(),
            "status": "OPERATIONAL"
        },
        "metrics": {
            "temperature_c": round(random.uniform(15.0, 30.0), 2),
            "humidity_pct": random.randint(40, 80),
            "network_latency_ms": random.randint(5, 120)
        }
    }

    # 3. Save Locally
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"sensor_{timestamp}.json")

    with open(file_path, "w") as f:
        json.dump(mock_data, f, indent=4)

    print(f"Success! Mock pipeline payload saved to: {file_path}")

except Exception as e:
    print(f"Unexpected local error: {e}")
