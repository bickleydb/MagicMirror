chown -R mysql:mysql /var/lib/mysql /var/run/mysqld
/etc/init.d/mysql start &
sleep 10
mysql -u root -e "GRANT ALL PRIVILEGES ON *.* TO'$DatabaseUser'@'%' IDENTIFIED BY '$DatabasePassword';"
/etc/init.d/mysql stop
mysqld