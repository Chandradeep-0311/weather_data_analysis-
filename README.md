# Weather Data API - README

This document provides an overview of the Weather Data API, including its setup, database schema, data ingestion process, API endpoints, and deployment considerations.

## 1. Prerequisites
Ensure you have the following installed before running the API:
- Python 3.x
- PostgreSQL
- Required Python libraries (FastAPI, SQLAlchemy, psycopg2, Flasgger)
)

## 2. Database Schema
The database consists of two tables:
- **weather_data**: Stores raw weather records.
- **weather_stats**: Stores aggregated yearly statistics.

## 3. Data Ingestion
Run the following Python script to ingest data from raw text files into the database:
```sh
python ingest_data.py
```

## 4. API Endpoints
The API provides the following endpoints:

### **1. Get Weather Data**
**Endpoint:** `GET /api/weather`

Retrieves weather records with optional filters.

**Query Parameters:**
- `station_id`: Filter by station ID
- `start_date`: Start date (YYYY-MM-DD)
- `end_date`: End date (YYYY-MM-DD)

### **2. Get Weather Statistics**
**Endpoint:** `GET /api/weather/stats`

Retrieves aggregated weather statistics.

**Query Parameters:**
- `station_id`: Filter by station ID
- `year`: Filter by year

## 5. Running the API
Start the FastAPI server using the command:
```sh
python app.py
```
Once the server is running, open **Swagger UI** to test the API:
```
http://127.0.0.1:5000/apidocs/
```
