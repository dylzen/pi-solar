# pi-solar

WARNING: this script is a work in progress and it's just for reference.

## Description

This is a script I decided to write for personal use.
It uses browser automation through Selenium to login to the inverter webapp and retrieving info on battery charge, status and more. Results are sent to the user via Telegram message.

Some data is imported from a config file that is not tracked.

## Installation

My use case is to add the following command to a crontab with the desired schedule. It will start the container, execute the script and then remove the container.

```bash
docker run --rm pi-solar
```

## Author

Dylan Tangredi\
[linkedin](https://www.linkedin.com/in/dylantangredi/)
