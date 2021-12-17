import logging
import os
from datetime import datetime

import salt.config
import salt.utils.event

from clients.factory import ShooterFactory

SHOOTER = os.environ.get('SHOOTER', 'KAFKA')

if __name__ == '__main__':
    opts = salt.config.client_config("/etc/salt/master")
    event = salt.utils.event.get_event("master", sock_dir=opts["sock_dir"], transport=opts["transport"], opts=opts)

    factory = ShooterFactory()
    shooter = factory.get_shooter(t=SHOOTER)

    while True:
        result = event.get_event(full=True)
        if result is None:
            continue

        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        logging.info(f'{SHOOTER.lower()} shooter: {current_time} --- {result}')
        shooter.shoot(key="saltstack", data=result)
