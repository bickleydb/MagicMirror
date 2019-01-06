FROM nginx
RUN apt-get clean
RUN apt-get update && apt-get -yq install python3 python3-pip nodejs git bash curl procps vim libpq-dev
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - 
RUN apt-get -yq install npm
RUN pip3 install virtualenv
RUN virtualenv MagicMirror
RUN pip3 install virtualenv && \
    pip3 install psycopg2 && \
    pip3 install Django && \
    pip3 install uwsgi && \
    pip3 install requests && \ 
    pip3 install python-twitter
 RUN npm install -g typescript && \
    npm install -g webpack && \
    npm install -g webpack-cli &&\
    npm install --save-dev @types/node
RUN mkdir /www/ /www/MagicMirror
COPY ./container_init.sh /www/MagicMirror/init.sh
COPY ./nginx_config/magicmirror_nginx.conf /etc/nginx/sites-available/
COPY ./nginx_config/uwsgi_params ./nginx_config/mime.types /www/
RUN chmod +777 /www/MagicMirror/init.sh
WORKDIR "/www/MagicMirror"
ENTRYPOINT [ "./init.sh" ]