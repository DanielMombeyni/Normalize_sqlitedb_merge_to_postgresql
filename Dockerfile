FROM python:3.11


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


WORKDIR /app


COPY requirements.txt .
COPY config.py .
COPY main.py .
COPY db/ db/
COPY normalization/ normalization/


RUN pip install --no-cache-dir -r requirements.txt


CMD ["python", "main.py"]
