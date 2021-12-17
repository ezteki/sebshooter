import os

from kafka import KafkaProducer

from clients.shooter import Shooter


class KafkaShooter(Shooter):
    def __init__(self):
        self.bootstrap_servers = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost')
        self.fallback_retry = os.environ.get('KAFKA_FALLBACK_RETRY', 5)
        self.username = os.environ.get('KAFKA_AUTH_USER')
        self.password = os.environ.get('KAFKA_AUTH_PASSWORD')
        self.protocol = os.environ.get('KAFKA_SECURITY_PROTOCOL', 'SASL_PLAINTEXT')
        self.mechanism = os.environ.get('KAFKA_SASL_MECHANISM', 'PLAIN')
        self.topic = os.environ.get('KAFKA_TOPIC', 'es-k8s-test')
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
        print(type(data))
        self.shooter.send(topic=self.topic, key=bytes(str(key).encode()), value=bytes(str(data).encode()))
