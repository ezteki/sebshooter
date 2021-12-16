import os

from kafka import KafkaProducer

from clients.shooter import Shooter

KAFKA_BOOTSTRAP_SERVERS = os.environ.get('KAFKA_BOOTSTRAP_SERVERS', 'localhost')
KAFKA_FALLBACK_RETRY = os.environ.get('KAFKA_FALLBACK_RETRY', 5)


class KafkaShooter(Shooter):

    def get_shooter(self):
        servers = KAFKA_BOOTSTRAP_SERVERS.split(";")
        return KafkaProducer(bootstrap_servers=servers, retries=5)

    def shoot(self, **kwargs):
        pass
