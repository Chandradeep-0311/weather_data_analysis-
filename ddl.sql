CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    station_id VARCHAR(20) NOT NULL,
    date DATE NOT NULL,
    max_temp DECIMAL(5,1),
    min_temp DECIMAL(5,1),
    precipitation DECIMAL(6,1),
    UNIQUE(station_id, date)
);

CREATE TABLE weather_stats (
    id SERIAL PRIMARY KEY,
    station_id VARCHAR(20) NOT NULL,
    year INT NOT NULL,
    avg_max_temp DECIMAL(5,2),
    avg_min_temp DECIMAL(5,2),
    total_precipitation DECIMAL(7,2),
    UNIQUE(station_id, year)
);
