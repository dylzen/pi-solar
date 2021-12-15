### first stage ####
FROM arm32v7/python:3.10 AS base

WORKDIR /solar-pi4-app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN pip install --user cryptography==3.3.2

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

### second stage ###
FROM arm32v7/python:3.10-slim-buster
COPY --from=base /root/.local /root/.local

WORKDIR /solar-pi4-app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get -y update \
    && apt-get install -y chromium \
    && apt-get install chromium-driver \
    && rm -r /var/lib/apt/lists/*

COPY ./app ./app

CMD ["python" , "./app/main.py"]