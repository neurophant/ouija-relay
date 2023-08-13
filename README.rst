Ouija Relay
===========

Ouija UDP relay with HTTPS proxy server interface built on top of `Ouija <https://github.com/neurophant/ouija>`_ library

Features
--------

Hides TCP traffic in encrypted UDP traffic between relay and proxy servers

.. image:: https://raw.githubusercontent.com/neurophant/ouija-relay/main/ouija.png
    :alt: UDP tunneling
    :width: 800

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
