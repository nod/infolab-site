#!/bin/sh

./manage.py runfcgi socket=/tmp/fcgi.infolab method=prefork \
        daemonize=true pidfile=/tmp/fcgi-infolab.pid

chmod 777 /tmp/fcgi.infolab # i hate this... -jk-
