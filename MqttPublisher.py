from paho.mqtt import publish
from paho.mqtt.client import MQTTv5


class MqttPublisher(object):

    def __init__(self, config: dict):
        self.hostname = config["hostname"]
        self.port = config["port"]
        self.auth = {'username': config["username"], 'password': config["password"]} if "username" in config and config["username"] else None
        self.topic_prefix = config["topic_prefix"]
        self.co2_value = None
        self.temperature = None

    def publish_if_new(self, co2_value: int, temperature: float) -> None:
        msgs = []
        if self.co2_value != co2_value:
            msgs.append(dict(topic=f"{self.topic_prefix}/co2", payload=co2_value, qos=1, retain=True))
            self.co2_value = co2_value
        if self.temperature != temperature:
            msgs.append(dict(topic=f"{self.topic_prefix}/temp", payload=temperature, qos=1, retain=True))
            self.temperature = temperature
        if msgs:
            publish.multiple(msgs, auth=self.auth, hostname=self.hostname, port=self.port, protocol=MQTTv5)
