#!/bin/bash
git clone https://github.com/dabickle/MagicMirror;
cd MagicMirror;

python3 ./manage.py makemigrations home splashpage statements timeapp traffic weather
python3 ./manage.py migrate

cd ./Javascript

npm install 
npm i @types/jquery
tsc

set -o xtrace

cd /www/MagicMirror/MagicMirror/Javascript/bundler
for filename in $(find -name *.webpack.config.js); do
   webpack --config $filename
done

cd /www/MagicMirror/MagicMirror/MagicMirror
cat settings.py linux_settings.txt > temp.out; cp temp.out settings.py

cd /www/MagicMirror/MagicMirror
python3 ./manage.py collectstatic
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('$AdminUsername', '$AdminEmail', '$AdminPass')" | python3 ./manage.py shell
uwsgi --socket :8001 --module MagicMirror.wsgi &
nginx -c /etc/nginx/sites-available/magicmirror_nginx.conf