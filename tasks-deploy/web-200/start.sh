#!/bin/bash

/etc/init.d/nginx restart
/etc/init.d/fcgiwrap restart

chmod 777 /var/run/fcgiwrap.socket

sleep infinity
