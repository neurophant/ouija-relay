import os
from enum import StrEnum

from cryptography.fernet import Fernet


class Protocol(StrEnum):
    TCP = 'TCP'
    UDP = 'UDP'


PROTOCOL = Protocol(os.getenv('OUIJA_PROTOCOL'))
DEBUG = bool(int(os.getenv('OUIJA_DEBUG')))
MONITOR = bool(int(os.getenv('OUIJA_MONITOR')))

RELAY_HOST = os.getenv('OUIJA_RELAY_HOST')
RELAY_PORT = int(os.getenv('OUIJA_RELAY_PORT'))
PROXY_HOST = os.getenv('OUIJA_PROXY_HOST')
PROXY_PORT = int(os.getenv('OUIJA_PROXY_PORT'))

KEY = os.getenv('OUIJA_KEY')
fernet = Fernet(KEY)
TOKEN = os.getenv('OUIJA_TOKEN')
SERVING_TIMEOUT = float(os.getenv('OUIJA_SERVING_TIMEOUT'))
TCP_BUFFER = int(os.getenv('OUIJA_TCP_BUFFER'))
TCP_TIMEOUT = float(os.getenv('OUIJA_TCP_TIMEOUT'))
MESSAGE_TIMEOUT = float(os.getenv('OUIJA_MESSAGE_TIMEOUT'))
UDP_PAYLOAD = int(os.getenv('OUIJA_UDP_PAYLOAD'))
UDP_TIMEOUT = float(os.getenv('OUIJA_UDP_TIMEOUT'))
UDP_RETRIES = int(os.getenv('OUIJA_UDP_RETRIES'))
UDP_CAPACITY = int(os.getenv('OUIJA_UDP_CAPACITY'))
UDP_RESEND_SLEEP = float(os.getenv('OUIJA_UDP_RESEND_SLEEP'))
