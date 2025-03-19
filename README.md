# Fitness Tracker Data Pipeline

A data engineering project showcasing AWS cloud skills by processing mock fitness tracker data.

## Project Structure
- `data/`: Local mock fitness data (e.g., `fitness_raw_data.csv`).
- `lambda/`: AWS Lambda function code.
- `scripts/`: Utility scripts (e.g., `generate_fitness_data.py`).

## AWS Setup
- **S3 Bucket**: `fitness-tracker-raw-data`
  - Region: `af-south-1`
  - Stores raw CSV files in `input/` folder.