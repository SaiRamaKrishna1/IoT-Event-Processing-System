FROM python:3.9

WORKDIR /app

COPY requirements.txt .

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
