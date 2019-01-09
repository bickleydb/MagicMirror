FROM amd64/ubuntu
RUN apt-get update && apt-get install -yq mysql-server ufw
RUN ufw allow mysql
RUN systemctl start mysql