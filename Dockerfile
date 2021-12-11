FROM arm32v7/python:3.10-buster

WORKDIR /solar-pi4-app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update && apt-get install -y chromium chromium-driver

RUN pip install --upgrade pip

RUN pip install cryptography==3.4.6 && pip install selenium==4.0.0 && pip install requests

COPY ./app ./app

CMD ["python" , "./app/main.py"]