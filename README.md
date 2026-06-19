# daily-learning-log
tracking my coding practices and skills transition

| Date | Focus Topic | What I Learned / Accomplished | Script |
| :--- | :--- | :--- | :--- |
| June 16, 2026 | Git Repository Setup | Initialized a centralized learning repository on GitHub to track data engineering progress and document daily technical milestones. | *(no script — git workflow)* |
| June 16, 2026 | Python ETL: Extract | Built a data ingestion script utilizing Python's `with open()` file I/O streams to read raw system logs line-by-line and track total record counts. | `extract_logs.py` |
| June 16, 2026 | Python ETL: Transform | Implemented conditional logic (`if ... in`) and Python indentation rules to filter a text data stream and isolate explicit network error states (`status:failed`). | `extract_logs2.py` |
| June 16, 2026 | Python ETL: Load | Completed an end-to-end text ETL pipeline by simultaneously managing multiple file I/O streams (`infile` and `outfile`) to isolate, transform, and export target data payloads. | `extract_logs3.py` |
| June 17, 2026 | Python Structured Data | Mastered the conceptual correlation that JSON text data maps directly to Python Dictionaries in memory. Used `json.load()` to extract nested device infrastructure data via key-value routing. | `parse_json.py` |
| June 17, 2026 | Python JSON Transformation | Combined JSON parsing with conditional loops to filter structured object arrays based on target key-value states. | `parse_json2.py` *(filtering logic added)* |
| June 17, 2026 | Python Data Aggregation | Mastered stateful tracking and metric aggregation by calculating total network capacity using conditional loops and variable accumulation. | `parse_json2.py` *(total_bandwidth accumulator)* |
| June 17, 2026 | Python Exception Handling | Implemented robust error-handling frameworks using `try/except` blocks to gracefully intercept `FileNotFoundError` states and prevent pipeline crashes. | `parse_json3.py` |
| June 17, 2026 | Python Modularization | Refactored standalone execution scripts into modular, reusable Python functions (`def`) to establish clean code standards. | `parse_json3.py` *(wrapped in `run_bandwidth_pipeline()`)* |
| June 17, 2026 | Python Parameterization | Upgraded modular functions to accept dynamic input arguments (`target_file`), making the ETL pipeline reusable across different data sources. | `network_pipeline.py` |
| June 17, 2026 | API Data Extraction | Integrated the `requests` library to ingest live HTTP JSON data payloads, implementing SSL verification bypasses and handling remote network response exceptions. | `api_pipeline.py` |
| June 17, 2026 | JSON Data Flattening | Mastered multi-layered JSON parsing by chaining dictionary keys to extract heavily nested attributes from live API payloads. | `api_pipeline_nestedjson.py` |
| June 17, 2026 | File Output (ETL Load) | Constructed a complete end-to-end ETL pipeline by writing transformed live API data into an external structured text file using Python file I/O operations. | `api_pipeline_load.py` |
| June 17, 2026 | Dataset Filtering & Serialization | Developed an optimized data-cleansing pipeline that parses real-world enterprise arrays, applies value-based filtering algorithms, and streams structured, serialized objects to a new target JSON file. | `api_production_etl.py` |
| June 18, 2026 | Algorithmic Sorting & Lambda Keys | Optimized pipeline performance by moving sorting operations out of iterative loops and utilizing Lambda evaluation functions for reverse-alphabetical data ordering. | `production_data_pipeline.py` *(`sorted(..., key=lambda ...)`)* |
| June 18, 2026 | Functional Architecture Refactoring | Modularized backend logic into an isolated, parameterized function framework, enabling multi-source generation from a single code deployment. | `production_data_pipeline.py` *(`production_data_pipeline(target_language, output_filename)` called twice)* |
| June 18, 2026 | Defensive Coding & Fault Tolerance | Hardened data ingestion pipelines against runtime KeyErrors by implementing dict `.get()` methods with custom string fallback defaults to handle missing or corrupt fields. | `production_data_pipeline_defensive.py` |
