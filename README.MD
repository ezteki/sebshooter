# Intro
`sebshooter` shoots saltstack event bus messages to where you want, support `KAFKA` right now !

# Required

```text
# which version saltstack depends
python>=3.6

kafka-python==2.0.2
salt==3004
```

# Install

```shell
$ pip3 install -r requirements.txt
```

# Config

```shell
# multi-servers split by `;`
KAFKA_BOOTSTRAP_SERVERS = ''
KAFKA_FALLBACK_RETRY = 5
KAFKA_AUTH_USER = ''
KAFKA_AUTH_PASSWORD = ''
KAFKA_TOPIC = ''
KAFKA_SECURITY_PROTOCOL = 'SASL_PLAINTEXT'
KAFKA_SASL_MECHANISM = 'PLAIN'
```

# Run

```shell
$ python3 main.py > /dev/null 2>&1
```

# Develop

Implement class `Shooter` like `KafkaShooter` do !
