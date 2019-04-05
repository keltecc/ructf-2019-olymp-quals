FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y nginx fcgiwrap && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN mkdir -p /var/www/task
WORKDIR /var/www/task

COPY ./service ./
RUN mv ./flag.txt /opt/flag.txt

RUN chmod 555 ./server.cgi && \
    chmod 444 /opt/flag.txt


CMD ["sleep infinity"]

EXPOSE 80
