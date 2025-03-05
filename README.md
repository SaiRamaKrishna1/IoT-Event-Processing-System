#IoT Event Processing System using MQTT and Docker

##Overview

##This project implements an IoT Event Processing System utilizing MQTT and Docker. The system consists of an MQTT broker, message validation, data storage, and a REST API, all containerized for efficient deployment

##Sample output
![Screenshot from 2025-03-06 03-00-37](https://github.com/user-attachments/assets/179d6bb1-a200-4fb1-aa02-5c61054b5f63)
![Screenshot from 2025-03-06 03-00-24](https://github.com/user-attachments/assets/5d0dde18-a6db-4fd8-a580-de6a95e38b18)


##System Architecture
![Screenshot from 2025-03-06 02-57-08](https://github.com/user-attachments/assets/a3ac52d8-ef73-448f-b580-5cdf9032a6d6)

##Documentation
## Installing Docker -- follow the process present in below link
https://docs.docker.com/engine/install/ubuntu/

## Pulling Docker image and Mosquito configuration, this configuration will be reflected on mosquitto container as we are exposing volume
``` docker pull eclipse-mosquitto
mkdir -p mosquitto/config
echo -e "listener 1883 0.0.0.0\nallow_anonymous true" > mosquitto/config/mosquitto.conf

## Run Docker compose in Deattached mode -- It will install the requirements and it will create the containers
``` docker compose up -d --build ```
