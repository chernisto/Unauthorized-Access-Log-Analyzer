FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY log_parser.py .
COPY apache_logs.txt .

CMD ["python", "log_parser.py"]
