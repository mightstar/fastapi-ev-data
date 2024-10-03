# Washington EV Data Aggregation API

This FastAPI application fetches electric vehicle data from the Washington State Department of Licensing and aggregates it by vehicle make for a given model year.

## Features

- Accepts a model year as a path parameter.
- Fetches data from the Washington State Electric Vehicle API.
- Aggregates the number of vehicles and the average electric range per vehicle make.
- Returns the aggregated data in JSON format.

## Setup Instructions

### 1. Clone the repository:

```bash
git clone <repository_url>
cd fastapi-ev-data
```

### 2. Set up a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### 4. Run the application:

```bash
unicorn main:app --reload
```

This will run the application locally at http://127.0.0.1:8000

### 5. Access the API:

You can access the API endpoint to get the data aggregated by vehicle make based on a model year. For example, to get data for the model year 2020, use this URL:

```bash
http://127.0.0.1:8000/ev-data/2020
```

### 6. Api Documentation:

FastAPI automatically generates API documentation. After running the application, you can visit the following URLs for documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## Example Request

```bash
/ev-data/{model_year}
```

- Model: GET
- Path Parameter: model_year(The model year of the vehicle, e.g., 2020)

## Example Response

```bash
{
   "model_year": 2020,
   "makes": [
       {
           "make": "Tesla",
           "vehicle_count": 250,
           "average_electric_range": 300
       },
       {
           "make": "Nissan",
           "vehicle_count": 150,
           "average_electric_range": 150
       }
   ]
}
```

## Error Handling

If no data is found for the given model year, the API will return a 404 status code with the following error message:

```bash
{
    "detail": "No data found for the specified model year."
}
```
