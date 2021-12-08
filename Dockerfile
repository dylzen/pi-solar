FROM arm32v7/python

WORKDIR /solar-pi4-app

ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN apt-get install -y chromium chromium-driver

RUN pip install cryptography==3.4.6

RUN pip install selenium

RUN pip install requests

COPY ./app ./app

CMD ["python" , "./app/main.py"]