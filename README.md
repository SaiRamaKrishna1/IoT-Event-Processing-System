# IoT Event Processing System using MQTT and Docker

## Overview

### This project implements an IoT Event Processing System utilizing MQTT and Docker. The system consists of an MQTT broker, message validation, data storage, and a REST API, all containerized for efficient deployment

## Sample output

![Screenshot from 2025-03-06 03-00-37](https://github.com/user-attachments/assets/179d6bb1-a200-4fb1-aa02-5c61054b5f63)

![Screenshot from 2025-03-06 03-00-24](https://github.com/user-attachments/assets/5d0dde18-a6db-4fd8-a580-de6a95e38b18)

## System Architecture
### The following flow diagram illustrates the architecture of the IoT Event Processing System:

![Screenshot from 2025-03-06 02-57-08](https://github.com/user-attachments/assets/a3ac52d8-ef73-448f-b580-5cdf9032a6d6)

## Installation and Setup
## Prerequisites
### Ensure that Docker is installed on your system. Follow the official Docker installation guide for Ubuntu

https://docs.docker.com/engine/install/ubuntu/

## Setting Up the MQTT Broker, Create the necessary Mosquitto configuration directory, Configure Mosquitto to allow anonymous connections and listen on port 1883

```
docker pull eclipse-mosquitto
git clone https://github.com/SaiRamaKrishna1/IoT-Event-Processing-System.git
cd IoT-Event-Processing-System/
mkdir -p mosquitto/config
echo -e "listener 1883 0.0.0.0\nallow_anonymous true" > mosquitto/config/mosquitto.conf
```

## Running the System with Docker Compose
### To build and run the system in detached mode, execute the following command:
```
docker compose up -d --build 
```
### This command installs the required dependencies and initializes the necessary containers

## Test Cases:
## Case 1: Valid Message
### Publishing a complete message and checking if it appears on the UI
```    
   mosquitto_pub -h localhost -p 1883 -t "/devices/events" -m '{
      "device_id": "device_100",
      "sensor_type": "temperature",
      "sensor_value": 25.5,
      "timestamp": "2025-03-06T12:30:00Z"
    }'
```
## Case 2: Missing Required Fields (Validation Error)
### Publishing an incomplete message and checking if it appears on the UI. If not, verify logs in the mqtt_client container logs
```   
   mosquitto_pub -h localhost -p 1883 -t "/devices/events" -m '{
      "device_id": "device_100",
      "sensor_value": 25.5,
      "timestamp": "2025-03-06T12:30:00Z"
    }'
```
## Case 3: JSON Syntax Error (Decoder Error)
### Publishing an incorrectly formatted message and checking for JSON decoding errors in mqtt_client logs
```
    mosquitto_pub -h localhost -p 1883 -t "/devices/events" -m '{
      "device_id": "device_100",
      sensor_type": "temperature",
      "sensor_value": 25.5,
      "timestamp": "2025-03-06T12:30:00Z"
    }'
```


