FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y xinetd libc6-i386 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


RUN useradd -M task


RUN mkdir /chroot
WORKDIR /chroot

RUN mkdir -p ./home/task/

RUN echo "cd /home/task/ && ./guessing" >./start.sh && \
    chmod 555 ./start.sh


RUN cp -R /lib* . && \
    cp -R /usr/lib* .

RUN mkdir ./dev && \
    mknod ./dev/null c 1 3 && \
    mknod ./dev/zero c 1 5 && \
    mknod ./dev/random c 1 8 && \
    mknod ./dev/urandom c 1 9 && \
    chmod 666 ./dev/*

RUN mkdir ./bin/ && \
    cp /bin/sh ./bin/ && \
    cp /bin/ls ./bin/ && \
    cp /bin/cat ./bin/ && \
    cp /bin/pwd ./bin/ && \
    cp /usr/bin/whoami ./bin/ && \
    ln -s /bin/sh ./bin/bash

RUN mkdir ./etc/ && \
    cp /etc/passwd ./etc/

RUN chown -R root:root .

COPY ./service ./home/task

RUN chmod 111 ./home/task/guessing && \
    chmod 444 ./home/task/flag.txt && \
    mv ./home/task/libc.so.6 ./lib/x86_64-linux-gnu/libc.so.6


COPY ./xinetd/xinetd.conf /etc/xinetd.d/service
COPY ./xinetd/start_xinetd.sh /start_xinetd.sh

RUN chmod 400 /etc/xinetd.d/service && \
    chmod 100 /start_xinetd.sh


CMD ["/start_xinetd.sh"]

EXPOSE 7777