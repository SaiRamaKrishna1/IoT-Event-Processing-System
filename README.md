![Screenshot from 2025-03-06 02-57-08](https://github.com/user-attachments/assets/a3ac52d8-ef73-448f-b580-5cdf9032a6d6)


# IoT-Event-Processing-System


IoT Event Processing System using MQTT and Docker

# Pulling MQTT docker image
docker pull eclipse-mosquitto

# Mosquito configuration, this configuration will be reflected on mosquitto container as we are exposing volume
mkdir -p mosquitto/config

echo -e "listener 1883 0.0.0.0\nallow_anonymous true" > mosquitto/config/mosquitto.conf

