#encoding=utf8
#! /bin/python

import psycopg2
import os

class PostgresDriverException(Exception):
    def __init__(self, code, msg):
        Exception.__init__(self)
        self.code = code
        self.msg = msg

class postgres_driver():
    def __init__(self):
        try:
            self.conn = psycopg2.connect(database=os.getenv('DB_NAME'), user=os.getenv('DB_LOGIN_NAME'), password=os.getenv('DB_LOGIN_PASS'), host=os.getenv('DB_HOST'))
            self.cur = self.conn.cursor()
        except Exception as e:
            raise PostgresDriverException(500, ("数据库链接失败:%s" % e))

    def __del__(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            pass

    def read(self, sql, argv = ''):
        try:
            self.cur.execute(sql, argv)
            return [dict((self.cur.description[i][0], value) for i, value in enumerate(row)) for row in self.cur.fetchall()]
        except Exception as e:
            raise PostgresDriverException(500, ("数据库读取失败:%s" % e))

    def write(self ,sql, argv= ''):
        try:
            self.cur.execute(sql, argv)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            raise PostgresDriverException(500, ("数据库写入失败:%s" % e))

    def write_ret_val(self):
        try:
            return self.cur.fetchone()[0]
        except Exception as e:
            raise PostgresDriverException(500, ("数据库写入返回值失败:%s" % e))
