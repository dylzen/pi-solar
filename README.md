# pi-solar

WARNING: this script is a work in progress and it's just for reference.

## Description

This is a script I decided to write for personal use.
It uses browser automation through Selenium to login to the inverter webapp and retrieving info on battery charge, status and more. Results are sent to the user via Telegram message.
At the moment the image is only built for armv7 architecture (like my Raspberry Pi 4).
Some sensitive data like passwords and tokens are passed through enviromnent variables to keep it safe.

## Installation

My use case is to add the following command to a crontab with the desired schedule. It will start the container, execute the script and then remove the container.

The --env-file flag is used to set environment variables in the container (they are listed ina file).

```bash
docker run --env-file env.list --rm dylzen/pi-solar
```

## Author

Dylan Tangredi\
[linkedin](https://www.linkedin.com/in/dylantangredi/)
