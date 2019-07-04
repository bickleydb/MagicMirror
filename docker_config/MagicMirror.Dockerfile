FROM nginx
ENV GoogleApiKey='' WeatherPrivateKey='' TwitterConsumerKey='' TwitterConsumerSecret='' TwitterAccessTokenKey='' TwitterAccessTokenSecret='' CountryCode='' ZipCode='' NumberPosts='' UserAgentString=''
RUN apt-get clean
RUN apt-get update && apt-get -yq install python3 python3-pip nodejs git bash curl procps vim libpq-dev python3-httplib2 python3-oauthlib
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - 
RUN apt-get -yq install npm
RUN pip3 install virtualenv
RUN virtualenv MagicMirror
RUN pip3 install virtualenv psycopg2 Django uwsgi requests python-twitter 
RUN npm install -g typescript webpack webpack-cli --save-dev @types/node
RUN mkdir /www/ /www/MagicMirror /etc/nginx/sites-available
COPY ./container_init.sh /www/MagicMirror/init.sh
COPY ./nginx_config/magicmirror_nginx.conf /etc/nginx/sites-available/
COPY ./nginx_config/uwsgi_params ./nginx_config/mime.types /www/
RUN chmod +777 /www/MagicMirror/init.sh
WORKDIR "/www/MagicMirror"
ENTRYPOINT [ "./init.sh" ]