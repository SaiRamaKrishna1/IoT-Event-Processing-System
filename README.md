# IoT-Event-Processing-System

IoT Event Processing System using MQTT and Docker

# Pulling MQTT docker image
docker pull eclipse-mosquitto

# Mosquito configuration, this configuration will be reflected on mosquitto container as we are exposing volume
mkdir -p mosquitto/config

echo -e "listener 1883 0.0.0.0\nallow_anonymous true" > mosquitto/config/mosquitto.conf

