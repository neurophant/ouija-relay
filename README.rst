Archived, replaced with `ouija-config <https://github.com/neurophant/ouija-config>`_

Ouija relay
===========

TCP and UDP relay with HTTPS proxy server interface configuration for `Ouija <https://github.com/neurophant/ouija>`_

Works in pair with `ouija-proxy <https://github.com/neurophant/ouija-proxy>`_

Features
--------

Hides TCP traffic in encrypted TCP/UDP traffic between relay and proxy servers

.. image:: https://raw.githubusercontent.com/neurophant/ouija-relay/main/ouija.png
    :alt: TCP/UDP tunneling
    :width: 800

Requirements
------------

* Python 3.11+
* Ouija 1.2.3

Setup - Ubuntu
--------------

.. code-block:: bash

    sudo apt install wget build-essential libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.11
    sudo apt-get install supervisor
    pip3 install ouija

    mkdir ouija-config
    # place your JSON config here
    touch ouija-config/relay.json

    git clone https://github.com/neurophant/ouija-relay.git
    cd ouija-relay
    sudo cp conf/ouija-relay.conf /etc/supervisor/conf.d/ouija-relay.conf
    sudo cp conf/supervisord.conf /etc/supervisor/supervisord.conf
    sudo systemctl restart supervisor.service
