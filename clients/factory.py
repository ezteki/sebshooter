from clients.kafka import KafkaShooter


class ShooterFactory(object):
    MAPPING = {
        'KAFKA': KafkaShooter
    }

    def get_shooter(self, t: str = 'KAFKA'):
        try:
            return self.MAPPING[t]().get_shooter()
        except KeyError:
            raise ModuleNotFoundError(f'{t} 类型的 Shooter 暂不支持')
