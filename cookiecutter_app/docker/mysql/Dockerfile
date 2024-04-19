FROM mysql:8.3

RUN usermod -u 1000 mysql
RUN chown -R mysql:mysql /var/lib/mysql

COPY /docker/mysql/init.sql /docker-entrypoint-initdb.d/init.sql

CMD ["mysqld"]
