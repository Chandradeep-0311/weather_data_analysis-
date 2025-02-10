from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flasgger import Swagger

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres_test:Temp1234@localhost/weather'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Swagger UI for API documentation
Swagger(app)  # Initialize Swagger UI

# Define WeatherData model to store raw weather records
class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.String(20))
    date = db.Column(db.Date)
    max_temp = db.Column(db.Float)
    min_temp = db.Column(db.Float)
    precipitation = db.Column(db.Float)

# Define WeatherStats model to store yearly aggregated weather statistics
class WeatherStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    station_id = db.Column(db.String(20))
    year = db.Column(db.Integer)
    avg_max_temp = db.Column(db.Float)
    avg_min_temp = db.Column(db.Float)
    total_precipitation = db.Column(db.Float)

# API Endpoint to retrieve weather data
@app.route('/API/weather', methods=['GET'])
def get_weather_data():
    """
    Get weather data
    ---
    parameters:
      - name: station_id
        in: query
        type: string
        required: false
        description: Filter by station ID
      - name: start_date
        in: query
        type: string
        format: date
        required: false
        description: Start date (YYYY-MM-DD)
      - name: end_date
        in: query
        type: string
        format: date
        required: false
        description: End date (YYYY-MM-DD)
    responses:
      200:
        description: A JSON object containing weather data
    """
    station_id = request.args.get('station_id')
    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    # Query building with optional filters
    query = WeatherData.query
    if station_id:
        query = query.filter(WeatherData.station_id == station_id)
    if start_date and end_date:
        query = query.filter(WeatherData.date.between(start_date, end_date))

    results = query.all()

    # Convert query results to JSON format
    return jsonify([{
        "station_id": w.station_id,
        "date": w.date.strftime("%Y-%m-%d"),
        "max_temp": w.max_temp,
        "min_temp": w.min_temp,
        "precipitation": w.precipitation
    } for w in results])

# API Endpoint to retrieve weather statistics
@app.route('/API/weather/stats', methods=['GET'])
def get_weather_stats():
    """
    Get weather statistics
    ---
    parameters:
      - name: station_id
        in: query
        type: string
        required: false
        description: Filter by station ID
      - name: year
        in: query
        type: integer
        required: false
        description: Filter by year
    responses:
      200:
        description: A JSON object containing weather statistics
    """
    station_id = request.args.get('station_id')
    year = request.args.get('year')

    # Query building with optional filters
    query = WeatherStats.query
    if station_id:
        query = query.filter(WeatherStats.station_id == station_id)
    if year:
        query = query.filter(WeatherStats.year == int(year))

    results = query.all()

    # Convert query results to JSON format
    return jsonify([{
        "station_id": w.station_id,
        "year": w.year,
        "avg_max_temp": w.avg_max_temp,
        "avg_min_temp": w.avg_min_temp,
        "total_precipitation": w.total_precipitation
    } for w in results])

# Run the Flask app in debug mode
if __name__ == '__main__':
    app.run(debug=True)
