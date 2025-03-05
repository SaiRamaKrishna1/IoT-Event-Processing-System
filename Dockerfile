FROM python:3.9

WORKDIR /app

COPY requirements.txt .

COPY mqtt_client.py .

RUN pip install --no-cache-dir -r requirements.txt

VOLUME ["/data"]

EXPOSE 1883

CMD ["python", "mqtt_client.py"]
