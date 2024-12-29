#!/usr/bin/env python3
import os
import sys
import time

import yaml

from Co2Device import Co2Device
from MqttPublisher import MqttPublisher


def get_config(config_file_path: str):
    with open(config_file_path, 'r') as stream:
        return yaml.load(stream, Loader=yaml.CLoader)


def main(device_path: str, config_file_path: str):
    config = get_config(config_file_path)

    monitor_device = Co2Device(device_path)
    monitor_device.open_monitor_device()

    publisher = MqttPublisher(config["mqtt"])

    while True:
        if data := monitor_device.read_device_data():
            publisher.publish_if_new(data.co2_level, data.temperature)

        time.sleep(config["read_time_interval"])


if __name__ == "__main__":
    script_base_dir = os.path.dirname(os.path.realpath(sys.argv[0])) + "/"
    config_file_path = script_base_dir + "config.yaml"

    device_path = sys.argv[1]

    main(device_path, config_file_path)
