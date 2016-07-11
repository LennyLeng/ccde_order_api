
FROM index.alauda.cn/lennyleng/flask-base

MAINTAINER Lenny Leng <admin@lennyleng.com>

RUN apt-get update
RUN apt-get -y install libpq-dev

RUN pip install flask_restful psycopg2 numpy
copy app /var/www/app
