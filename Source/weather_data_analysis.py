import psycopg2

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


def calculate_weather_stats():
    """
    Calculates yearly weather statistics for each station and inserts the aggregated data
    into the 'weather_stats' table.

    - Computes:
      1. Average maximum temperature (`avg_max_temp`)
      2. Average minimum temperature (`avg_min_temp`)
      3. Total precipitation (`total_precipitation`)
    - Filters out NULL values before aggregation.
    - Ensures no duplicate entries by using `ON CONFLICT DO NOTHING` to avoid redundant inserts.
    """
    # Establish database connection
    conn = connect_db()
    cursor = conn.cursor()

    # SQL query to calculate yearly weather statistics
    cursor.execute("""
        INSERT INTO weather_stats (station_id, year, avg_max_temp, avg_min_temp, total_precipitation)
        SELECT 
            station_id, 
            EXTRACT(YEAR FROM date) AS year,
            AVG(max_temp) AS avg_max_temp,
            AVG(min_temp) AS avg_min_temp,
            SUM(precipitation) AS total_precipitation
        FROM weather_data
        WHERE max_temp IS NOT NULL 
          AND min_temp IS NOT NULL 
          AND precipitation IS NOT NULL
        GROUP BY station_id, year
        ON CONFLICT (station_id, year) DO NOTHING;
    """)

    # Commit changes to the database
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


# Execute the weather statistics calculation
calculate_weather_stats()
