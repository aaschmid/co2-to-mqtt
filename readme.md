# Requirements

## Hardware

1) [TFA-Dostmann AirControl Mini CO2 Messgerät](http://www.amazon.de/dp/B00TH3OW4Q)

2) Any Linux system with a USB port and Python 3

# Installation

1) Install Python and dependencies (needs `sudo`)

```
make install-debian
make install-dependencies  # pip dependencies
```

2) Create a configuration file with all required information (see `config.yaml.sample` for the
   precise file structure)

Please note: Currently authentication or else is not supported for MQTT.

3) Fix socket permissions: install udev rules
```
make setup-udev
```

4) Run the script
```
make run
```
The configuration is named `config.yaml` and should be in the same directory as the script.


# Credits

Heavily inspired by [OlafMerkert/office_weather](https://github.com/OlafMerkert/office_weather) who
forked from [wooga/office_weather](https://github.com/wooga/office_weather), which in turn is based on code by [henryk ploetz](https://hackaday.io/project/5301-reverse-engineering-a-low-cost-usb-co-monitor/log/17909-all-your-base-are-belong-to-us).


# License

[MIT](http://opensource.org/licenses/MIT)
