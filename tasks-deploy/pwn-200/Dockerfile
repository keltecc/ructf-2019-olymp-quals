FROM ubuntu:18.04


RUN apt-get update

RUN apt-get install -y xinetd && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN useradd -M task


COPY ./xinetd/xinetd.conf /etc/xinetd.d/service
COPY ./xinetd/start_xinetd.sh /start_xinetd.sh

RUN chmod 400 /etc/xinetd.d/service && \
    chmod 100 /start_xinetd.sh


RUN mkdir -p /service/

WORKDIR /service/

COPY ./service/ ./


RUN chmod 111 ./bandit && \
    chmod 444 ./flag.txt


CMD ["/start_xinetd.sh"]

EXPOSE 7777
