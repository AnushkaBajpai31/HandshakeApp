from Logging.Breadcrumb import Breadcrumb
from Database.QueryBuilder import QueryTypes, QueryBuilder
from Database.SqlDatabase import SqlDatabase
from config import DEBUG
from constants import *

class BaseDataAccess:
    def __init__(self):
        self.db = SqlDatabase()
        self.start()
        self.queryBuilder = QueryBuilder()
        self.queryTypes = QueryTypes

    def start(self):
        if DEBUG:
            Breadcrumb.throw_crumb(CREATING_CONNECTION)
        self.db.create_connection()
        self.db.get_cursor()

    def mark_as_done(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def begin(self):
        self.db.begin()

    def stop(self):
        if DEBUG:
            Breadcrumb.throw_crumb(CLOSING_CONNECTION)
        self.db.close_connection()

    def insert(self, query, values):
        try:
            self.db.begin()
            self.db.execute_query(query, values)
            self.db.commit()
            if DEBUG:
                Breadcrumb.throw_crumb(INSERT_SUCCESS)
            return self.db.fetchone()
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(INSERT_FAILED)
                print(e)
            self.db.rollback()
            raise e

    def update(self, query):
        try:
            self.db.begin()
            self.db.execute_query(query)
            self.db.commit()
            if DEBUG:
                Breadcrumb.throw_crumb(UPDATE_SUCCESS)
            return self.db.fetchone()
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(UPDATE_FAILED)
                print(e)
            self.db.rollback()
            raise e

    def delete(self, query, values=None):
        try:
            self.db.begin()
            self.db.execute_query(query, values)
            self.db.commit()
            if DEBUG:
                Breadcrumb.throw_crumb(DELETE_SUCCESS)
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(DELETE_FAILED)
                print(e)
            self.db.rollback()
            raise e

    def get_many(self, query):
        try:
            self.db.execute_query(query)
            return self.db.fetchall()
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(GET_FAILED)
                print(e)
            raise e

    def get(self, query, values):
        try:
            self.db.execute_query(query, values)
            return self.db.fetchone()
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(GET_FAILED)
                print(e)
            raise e

    def get_descriptions(self):
        return self.db.get_cursor().description

