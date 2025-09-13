FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install requirements.txt

COPY log_parser.py .

CMD ["python", "log_parser.py"]
