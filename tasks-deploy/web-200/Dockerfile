FROM ubuntu:18.04

RUN apt update
RUN apt install -y nginx
RUN apt install -y fcgiwrap


COPY ./start.sh /start.sh

RUN mv ./flag.txt /opt/flag.txt

RUN /etc/init.d/fcgiwrap restart

RUN chmod 555 /var/www/task/server.cgi && \
    chmod 444 /opt/flag.txt && \
    chmod 777 /var/run/fcgiwrap.socket && \
    chmod 555 /start.sh


CMD ["/start.sh"]

EXPOSE 80
