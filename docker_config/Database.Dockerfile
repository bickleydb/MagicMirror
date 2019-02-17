FROM arm32v7/ubuntu
RUN apt-get update && apt-get install -yq mysql-server ufw less git

RUN mkdir -p /var/run/mysqld
RUN chown mysql:mysql /var/run/mysqld
RUN git clone https://github.com/mysql/mysql-docker.git

COPY init.sh init.sh
RUN chmod +777 init.sh
COPY mysqld.cnf /etc/mysql/mysql.conf.d/mysqld.cnf
ENTRYPOINT [ "sh", "./init.sh" ]

