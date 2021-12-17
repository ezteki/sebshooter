import logging
import os

import salt.config
import salt.utils.event

from clients.factory import ShooterFactory

logger = logging.getLogger()

SHOOTER = os.environ.get('SHOOTER', 'KAFKA')

if __name__ == '__main__':
    opts = salt.config.client_config("/etc/salt/master")
    event = salt.utils.event.get_event("master", sock_dir=opts["sock_dir"], transport=opts["transport"], opts=opts)

    factory = ShooterFactory()
    shooter = factory.get_shooter(t=SHOOTER)

    shooter.shoot(data={"a": 1})
    while True:
        result = event.get_event(full=True)
        if result is None:
            continue

        logger.info(result)
        shooter.shoot(data=result)
