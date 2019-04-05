FROM ubuntu:18.04

RUN apt update
RUN apt install -y nginx
RUN apt install -y fcgiwrap


COPY ./start.sh /start.sh
COPY ./service /var/www/task/
COPY ./nginx/nginx.conf /etc/nginx/sites-available/default
COPY ./fcgiwrap/fcgiwrap.init /etc/init.d/fcgiwrap


RUN mv /var/www/task/flag.txt /opt/flag.txt

RUN chmod 555 /var/www/task/server.cgi && \
    chmod 444 /opt/flag.txt && \
    chmod 555 /start.sh && \
    chmod 777 /var/www/task/files/


CMD ["/start.sh"]

EXPOSE 80
