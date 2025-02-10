import os
import psycopg2
from datetime import datetime

# Database Configuration
DB_CONFIG = {
    "dbname": "weather",  # Name of the PostgreSQL database
    "user": "postgres_test",  # Database username
    "password": "Temp1234",  # Database password
    "host": "localhost"  # Database host (running locally)
}


def connect_db():
    """
    Establishes a connection to the PostgreSQL database.

    Returns:
        psycopg2.connection: A connection object to interact with the database.
    """
    return psycopg2.connect(**DB_CONFIG)


def ingest_weather_data(file_path):
    """
    Reads weather data from a text file and inserts it into the 'weather_data' table.

    Each line in the file contains:
        1. The date (YYYYMMDD)
        2. The maximum temperature for that day (in tenths of a degree Celsius)
        3. The minimum temperature for that day (in tenths of a degree Celsius)
        4. The amount of precipitation for that day (in tenths of a millimeter)

    Missing values are represented as `-9999` and are converted to NULL.

    The function ensures:
    - Duplicate records are not inserted (using `ON CONFLICT (station_id, date) DO NOTHING`).
    - Logs the start and end times of the ingestion process.

    Args:
        file_path (str): The path to the weather data file.
    """
    # Establish database connection
    conn = connect_db()
    cursor = conn.cursor()

    start_time = datetime.now()  # Start time for logging performance

    # Open the file and read data line by line
    with open(file_path, "r") as file:
        for line in file:
            parts = line.strip().split()  # Split line by whitespace
            station_id = os.path.basename(file_path).split(".")[0]  # Extract station ID from filename
            date = parts[0]  # Date in YYYYMMDD format
            max_temp = None if int(parts[1]) == -9999 else int(parts[1]) / 10.0  # Convert tenths of degrees to Celsius
            min_temp = None if int(parts[2]) == -9999 else int(parts[2]) / 10.0  # Convert tenths of degrees to Celsius
            precipitation = None if int(parts[3]) == -9999 else int(parts[3]) / 10.0  # Convert tenths of mm to mm

            # Insert data into the database, avoiding duplicates
            cursor.execute("""
                INSERT INTO weather_data (station_id, date, max_temp, min_temp, precipitation)
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (station_id, date) DO NOTHING;
            """, (station_id, date, max_temp, min_temp, precipitation))

    # Commit the transaction to save changes
    conn.commit()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Log the completion time and duration
    print(f"Data ingestion completed for {file_path} in {datetime.now() - start_time}")


# Directory containing the weather data files
data_dir = "~/Downloads/code-challenge-template-main/weather_data/"

# Iterate over all text files in the directory and ingest them
for file in os.listdir(data_dir):
    if file.endswith(".txt"):
        ingest_weather_data(os.path.join(data_dir, file))
