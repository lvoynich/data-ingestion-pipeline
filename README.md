# Local Automated Data Ingestion Pipeline

A robust, local data engineering pipeline built to ingest real-time streaming data, process telemetry metrics, and store unstructured payloads securely. This project demonstrates modular Python script design, robust exception handling, and structural data version control.

## 🛠️ Architecture & Tech Stack
* **Language:** Python 3 (Object-Oriented & Scripting)
* **Ingestion Layer:** Python `requests` with custom error catch blocks
* **Version Control:** Git & GitHub
* **Target Environment:** macOS (Native Unix)

## 📁 Repository Structure
* `ingest.py`: Core ingestion engine with simulated failure recovery and local mock payload generation.
* `.gitignore`: Configured environment protection tracking to explicitly isolate raw data directories from production codebase deployment.

## 🚀 Getting Started & Execution

1. Clone this repository to your local Mac directory.
2. Install the necessary ingestion packages:
   ```bash
   pip3 install requests
   ```
3. Execute the pipeline processing script:
   ```bash
   python3 ingest.py
   ```

## 📈 Future Pipeline Roadmap
* **Phase 2:** Integrate Apache PySpark to ingest local directories and run distributed data transformations.
* **Phase 3:** Establish local MongoDB NoSQL cluster nodes to serve as the long-term persistent storage target.
