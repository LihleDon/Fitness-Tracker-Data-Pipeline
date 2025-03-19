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

  ## Pipeline Workflow
- **S3 Trigger**: Uploads to `input/` folder (e.g., `fitness_raw_data.csv`) trigger `FitnessDataAggregator`.
- **Lambda**: Aggregates steps and calories by user and date, stores in DynamoDB.
- **DynamoDB**: Stores daily summaries (e.g., `user_id: user001, date: 2025-03-01, total_steps: 12345, total_calories: 617.25`).
- **CloudWatch**: Optional daily run at 8 AM UTC.

## Free Tier Compliance
- S3: < 5 GB (mock data ~10 KB).
- Lambda: < 750,000 seconds/month (few executions).
- DynamoDB: < 25 GB, 5 write units (well within limits).