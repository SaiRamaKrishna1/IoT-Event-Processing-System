# IoT Event Processing System using MQTT and Docker

## Overview

## This project implements an IoT Event Processing System utilizing MQTT and Docker. The system consists of an MQTT broker, message validation, data storage, and a REST API, all containerized for efficient deployment

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

```docker pull eclipse-mosquitto
mkdir -p mosquitto/config
echo -e "listener 1883 0.0.0.0\nallow_anonymous true" > mosquitto/config/mosquitto.conf
```

## Running the System with Docker Compose
### To build and run the system in detached mode, execute the following command:

```docker compose up -d --build```
### This command installs the required dependencies and initializes the necessary containers
