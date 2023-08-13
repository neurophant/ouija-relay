Ouija relay
===========

Ouija UDP relay with HTTPS proxy server interface built on top of `Ouija <https://github.com/neurophant/ouija>`_ library

Features
--------

Hides TCP traffic in encrypted UDP traffic between relay and proxy servers

.. image:: https://raw.githubusercontent.com/neurophant/ouija-relay/main/ouija.png
    :alt: UDP tunneling
    :width: 800

Environment variables
---------------------

* OUIJA_DEBUG: 0 - error logging, 1 - debug logging
* OUIJA_MONITOR: 0 - monitor off, 1 - monitor on
* OUIJA_RELAY_HOST: ouija relay host/ip addr
* OUIJA_RELAY_PORT: ouija relay port
* OUIJA_PROXY_HOST: ouija proxy host/ip addr
* OUIJA_PROXY_PORT: ouija proxy port
* OUIJA_KEY: Fernet secret key, use Fernet.generate_key()
* OUIJA_TOKEN: your secret token - UUID4 or anything else
* OUIJA_SERVING_TIMEOUT: timeout for serve/resend workers, 2X for handlers, seconds
* OUIJA_TCP_BUFFER: TCP buffer size, bytes
* OUIJA_TCP_TIMEOUT: TCP awaiting timeout, seconds
* OUIJA_UDP_PAYLOAD: UDP payload size, bytes
* OUIJA_UDP_TIMEOUT: UDP awaiting timeout, seconds
* OUIJA_UDP_RETRIES: UDP max retry count per interaction
* OUIJA_UDP_CAPACITY: UDP send/receive buffer capacity - max packet count
* OUIJA_UDP_RESEND_SLEEP: UDP resend sleep between retries, seconds

.. code-block:: bash

    export OUIJA_DEBUG="1"
    export OUIJA_MONITOR="1"
    export OUIJA_RELAY_HOST="127.0.0.1"
    export OUIJA_RELAY_PORT="9000"
    export OUIJA_PROXY_HOST="127.0.0.1"
    export OUIJA_PROXY_PORT="50000"
    export OUIJA_KEY="bdDmN4VexpDvTrs6gw8xTzaFvIBobFg1Cx2McFB1RmI="
    export OUIJA_TOKEN="secret"
    export OUIJA_SERVING_TIMEOUT="30.0"
    export OUIJA_TCP_BUFFER="1024"
    export OUIJA_TCP_TIMEOUT="1.0"
    export OUIJA_UDP_PAYLOAD="1024"
    export OUIJA_UDP_TIMEOUT="3.0"
    export OUIJA_UDP_RETRIES="5"
    export OUIJA_UDP_CAPACITY="1000"
    export OUIJA_UDP_RESEND_SLEEP="0.5"

Requirements
------------

* Python 3.11+
* Ouija 1.1.0

Setup - Ubuntu
--------------

.. code-block:: bash

    sudo apt install wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.11
    sudo apt-get install supervisor

    git clone https://github.com/neurophant/ouija-relay.git
    cd ouija-relay
    sudo cp conf/ouija-relay.conf /etc/supervisor/conf.d/ouija-relay.conf
    sudo cp conf/supervisord.conf /etc/supervisor/supervisord.conf
    sudo systemctl restart supervisor.service
