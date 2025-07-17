from flask import Flask, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

# Fixed route: Rajiv Chowk → ITO → Akshardham
route = [
    (28.6328, 77.2197),
    (28.6295, 77.2226),
    (28.6280, 77.2300),
    (28.6270, 77.2370),
    (28.6289, 77.2425),
    (28.6220, 77.2490),
    (28.6180, 77.2600),
    (28.6129, 77.2773)
]

# Track current index for each bus
bus_positions = {
    "101": 0,
    "102": 0
}

@app.route('/api/buses')
def get_buses():
    buses_data = {}

    for bus_id in bus_positions:
        index = bus_positions[bus_id]
        lat, lon = route[index]
        speed = 30 if bus_id == "101" else 25  # Different speed if needed

        # Move to next position
        bus_positions[bus_id] = (index + 1) % len(route)

        buses_data[bus_id] = {
            "lat": lat,
            "lon": lon,
            "speed": speed,
            "last_updated": time.time()
        }

    return jsonify(buses_data)

if __name__ == '__main__':
    app.run(debug=True)
