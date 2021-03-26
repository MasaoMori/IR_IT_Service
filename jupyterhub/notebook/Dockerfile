FROM jupyter/r-notebook:7e07b801d92b

USER root

ENV DEBIAN_FRONTEND noninteractive
WORKDIR /tmp
RUN wget -c https://dev.mysql.com/get/mysql-apt-config_0.8.16-1_all.deb \
 && apt-get update \
 && apt-get install lsb-release -y \
    gnupg
RUN dpkg -i mysql-apt-config_0.8.16-1_all.deb \
 && apt-get update \
 && apt-get install mysql-client -y
ENV DEBIAN_FRONTEND dialog

WORKDIR $HOME
