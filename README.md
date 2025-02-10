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

## (Extra Credit)- AWS API Deployment Approach

### **1. Database Hosting**
- Use **Amazon RDS (PostgreSQL)** for scalable and secure data storage.

### **2. API Deployment**
- Deploy the API using **AWS Lambda** for a serverless approach or **Amazon EC2** for full infrastructure control.

### **3. Data Ingestion**
- Automate data ingestion with **AWS Glue** for batch processing.
- Use **AWS Lambda** for real-time event-driven data processing.

### **4. Containerization**
- Use **Docker** to containerize the API, ensuring consistency and portability across environments.

### **5. Scalability & Security**
- Enable **auto-scaling** for API instances and database resources.
- Manage access control and security with **AWS IAM** and **Secrets Manager**.

---

