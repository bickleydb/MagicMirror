FROM amd64/ubuntu
RUN apt-get update && apt-get install -yq mysql-server ufw less git

RUN mkdir -p /var/run/mysqld
RUN chown mysql:mysql /var/run/mysqld
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
RUN git clone https://github.com/mysql/mysql-docker.git

ENV USER=mirror
ENV MYSQL_DATABASE=mirror
ENV MYSQL_USER=mirror

COPY init.sh init.sh
RUN chmod +777 init.sh

EXPOSE 3306 33060

