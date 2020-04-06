FROM python:3.8-slim-buster as builder

WORKDIR /code

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080
CMD ["python", "app.py"]