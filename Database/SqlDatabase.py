from psycopg2 import connect
from Logging.Breadcrumb import Breadcrumb
from config import DEBUG
from constants import *


class SqlDatabase:
    def __init__(self):
        self.conn = None
        self.cursor = None

    def create_connection(self):
        try:
            if not self.conn:
                conn = connect(host="localhost", user="postgres", password="admin", dbname="handshakedb")
                self.conn = conn
            return self.conn
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(CONNECTION_FAILURE)
                print(e)
            raise e

    def get_cursor(self):
        if not self.cursor:
            cursor = self.conn.cursor()
            self.cursor = cursor
        return self.cursor

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def commit(self):
        self.conn.commit()

    def rollback(self):
        self.conn.rollback()

    def begin(self):
        self.conn.autocommit = False

    def execute_query(self, query, values=None):
        try:
            if values:
                self.cursor.mogrify(query, values)
            self.cursor.execute(query)
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(QUERY_FAILURE)
                print(e)
            raise e

    def fetchall(self):
        try:
            return self.cursor.fetchall()
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(FETCH_ALL_FAILURE)
                print(e)
            raise e

    def fetchone(self):
        try:
            return self.cursor.fetchone()
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(FETCH_FAILURE)
                print(e)
            raise e
