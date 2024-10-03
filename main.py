from fastapi import FastAPI, HTTPException
import requests
from collections import defaultdict

app = FastAPI()

# External API URL (EV data)
EV_DATA_URL = "https://data.wa.gov/resource/f6w7-q2d2.json"

@app.get("/ev-data/{model_year}")
def get_ev_data(model_year: int):
    # Fetch data from external API
    try:
        response = requests.get(EV_DATA_URL)
        response.raise_for_status()  # Raise an exception for bad status codes
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch data: {str(e)}")

    ev_data = response.json()

    # Filter the data based on the model year and aggregate by make
    aggregated_data = defaultdict(lambda: {'count': 0, 'total_range': 0})

    for vehicle in ev_data:
        if vehicle.get("model_year") and int(vehicle["model_year"]) == model_year:
            make = vehicle.get("make", "Unknown")
            electric_range = vehicle.get("electric_range", 0)
            
            aggregated_data[make]['count'] += 1
            aggregated_data[make]['total_range'] += int(electric_range) if electric_range else 0

    # Prepare the response: number of vehicles and average range per make
    result = []
    for make, data in aggregated_data.items():
        count = data['count']
        avg_range = data['total_range'] / count if count > 0 else 0
        result.append({
            "make": make,
            "vehicle_count": count,
            "average_electric_range": avg_range
        })

    if not result:
        raise HTTPException(status_code=404, detail="No data found for the specified model year.")

    return {"model_year": model_year, "makes": result}