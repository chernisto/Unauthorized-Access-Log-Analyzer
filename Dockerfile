FROM python:3.13-slim

WORKDIR /app

COPY requirenments.txt .
RUN pip install --upgrade pip && pip install requirenments.txt

COPY log_parser.py .

CMD ["python", "log_parser.py"]
