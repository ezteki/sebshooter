import json

from kafka import KafkaProducer

from clients.config import KAFKA_TOPIC, KAFKA_AUTH_PASSWORD, KAFKA_FALLBACK_RETRY, KAFKA_AUTH_USER, \
    KAFKA_BOOTSTRAP_SERVERS, KAFKA_SASL_MECHANISM, KAFKA_SECURITY_PROTOCOL
from clients.shooter import Shooter


class KafkaShooter(Shooter):
    def __init__(self):
        self.bootstrap_servers = KAFKA_BOOTSTRAP_SERVERS or 'localhost'
        self.fallback_retry = KAFKA_FALLBACK_RETRY or 5
        self.username = KAFKA_AUTH_USER
        self.password = KAFKA_AUTH_PASSWORD
        self.protocol = KAFKA_SECURITY_PROTOCOL
        self.mechanism = KAFKA_SASL_MECHANISM
        self.topic = KAFKA_TOPIC
        self.shooter = None

    def init_shooter(self):
        servers = self.bootstrap_servers.split(";")
        config = {
            'bootstrap_servers': servers,
            'retries': self.fallback_retry,
            'sasl_mechanism': self.mechanism,
            'security_protocol': self.protocol,
            'sasl_plain_username': self.username,
            'sasl_plain_password': self.password
        }
        self.shooter = KafkaProducer(**config)

    def shoot(self, key, data):
        self.shooter.send(topic=self.topic,
                          key=bytes(str(key).encode()),
                          value=bytes(json.dumps(data).encode()))
