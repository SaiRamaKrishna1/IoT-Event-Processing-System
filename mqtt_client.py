import time
import json, os
import sqlite3
import logging
import asyncio
from jsonschema import validate, ValidationError
from datetime import datetime
from gmqtt import Client as MQTTClient

# Broker address or localhost
BROKER_HOST = os.getenv("BROKER_HOST", "mqtt_broker")
BROKER_PORT = int(os.getenv("BROKER_PORT", 1883)) 
# Topic
TOPIC = "/devices/events"

# File name
file_name = "mqtt_client.log"

logging.basicConfig(filename=file_name, level=logging.INFO, format="%(asctime)s - %(message)s")


DB_NAME = "/data/mqtt_data.db"

# JSON schema for validation
schema = {
    "type": "object",
    "properties": {
        "device_id": {"type": "string"},
        "sensor_type": {"type": "string"},
        "sensor_value": {"type": "number"},
        "timestamp": {
            "type": "string",
            "format": "date-time"
        }
    },
    "required": ["device_id", "sensor_type", "sensor_value", "timestamp"]
}

# Creating DB and Table if not present
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Devices (
            device_id TEXT PRIMARY KEY,
            last_seen TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            sensor_type TEXT,
            sensor_value REAL,
            timestamp TEXT,
            FOREIGN KEY(device_id) REFERENCES Devices(device_id)
        )
    """)
    conn.commit()
    conn.close()

# Function to insert valid data into the database
def store_data(data):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Update device last seen time
    cursor.execute("""
        INSERT INTO Devices (device_id, last_seen)
        VALUES (?, ?)
        ON CONFLICT(device_id) DO UPDATE SET last_seen = excluded.last_seen
    """, (data["device_id"], data["timestamp"]))

    # Insert sensor event
    cursor.execute("""
        INSERT INTO Events (device_id, sensor_type, sensor_value, timestamp)
        VALUES (?, ?, ?, ?)
    """, (data["device_id"], data["sensor_type"], data["sensor_value"], data["timestamp"]))

    conn.commit()
    conn.close()

# Function to process MQTT messages
async def on_message(client, topic, payload, qos, properties):
    try:
        message = json.loads(payload)
        logging.info(f"Received message: {message}")
        validate(instance=message, schema=schema)
        logging.info(f"message validated: {message}")
        store_data(message)
    except ValidationError as e:
        logging.info(f"Validation error: {e} - Payload: {payload}")
    except json.JSONDecodeError as e:
        logging.info(f"JSON decoding error: {e} - Payload: {payload}")

async def main():
    client = MQTTClient("mqtt_listener")
    client.on_message = on_message  
    while True:
        try:
            logging.info("Connecting to MQTT Broker")
            await client.connect(BROKER_HOST, BROKER_PORT)
            await asyncio.sleep(1) 
            client.subscribe(TOPIC)
            logging.info(f"Subscribed to topic: {TOPIC}")
            while True:
                await asyncio.sleep(1) 

        except Exception as e:
            logging.info(f"MQTT Connection Error: {e}")
            logging.info(f"MQTT Connection Error: {e}")
            await asyncio.sleep(5)

# Initializing DB and starting MQTT
if __name__ == "__main__":
    logging.info("Intializing broker")
    init_db()
    asyncio.run(main())
