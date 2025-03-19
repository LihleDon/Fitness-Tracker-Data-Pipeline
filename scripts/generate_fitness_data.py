import csv
import random
from datetime import datetime, timedelta

# Generate mock fitness data for March 2025
def generate_mock_data(filename, num_rows=100):
    headers = ["user_id", "timestamp", "steps", "calories"]
    start_date = datetime(2025, 3, 1)
    
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        
        for _ in range(num_rows):
            user_id = f"user{random.randint(1, 10):03d}"  # e.g., user001 to user010
            time_offset = timedelta(days=random.randint(0, 18), hours=random.randint(0, 23))
            timestamp = (start_date + time_offset).strftime("%Y-%m-%d %H:%M:%S")
            steps = random.randint(500, 15000)
            calories = round(steps * 0.05, 2)  # Rough estimate: 0.05 cal per step
            writer.writerow([user_id, timestamp, steps, calories])

if __name__ == "__main__":
    generate_mock_data("fitness_raw_data.csv")