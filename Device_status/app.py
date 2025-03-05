from flask import Flask, jsonify, request, render_template
import sqlite3
import logging

app = Flask(__name__, template_folder="templates", static_folder="static")

DB_NAME = "/data/mqtt_data.db"

# Configure logging
file_name = "events.log"

logging.basicConfig(filename=file_name, level=logging.INFO, format="%(asctime)s - %(message)s")


# Function to query the database safely
def query_db(query, args=(), one=False):
    try:
        with sqlite3.connect(DB_NAME) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute(query, args)
            result = cur.fetchall()
            return (result[0] if result else None) if one else result
    except sqlite3.Error as e:
        logging.info(f"Database error: {e}")
        return []


# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Endpoint to list all registered devices with last seen timestamps
@app.route("/devices", methods=["GET"])
def list_devices():
    logging.info(f"Devices Api called")
    devices = query_db("SELECT * FROM Devices")
    return render_template("devices.html", devices=devices)


# Endpoint to retrieve the latest events for a given device
@app.route("/devices/<device_id>/events", methods=["GET"])
def get_device_events(device_id):
    logging.info(f"Events Api called and device id {device_id}")
    limit = request.args.get("limit", 10, type=int)
    events = query_db(
        "SELECT * FROM Events WHERE device_id = ? ORDER BY timestamp DESC LIMIT ?",
        (device_id, limit),
    )
    return render_template("events.html", events=events, device_id=device_id)


if __name__ == "__main__":
    logging.info(f"app is running")
    app.run(host="0.0.0.0", port=5000, debug=True)
