from DataAccess.BaseDataAccess import BaseDataAccess
from Logging.Breadcrumb import Breadcrumb
from config import DEBUG
from constants import *


class Student(BaseDataAccess):
    TABLE = "students"
    ID_COL = "id"
    FIRST_NAME_COL = "first_name"
    LAST_NAME_COL = "last_name"
    CHECK_IN_COL = "check_in_time"

    def __init__(self):
        super().__init__()

    def insert_student(self, data_model):
        try:
            query = self.queryBuilder.build(self.queryTypes.INSERT, self.TABLE, [self.FIRST_NAME_COL, self.LAST_NAME_COL, self.CHECK_IN_COL])
            _id = self.insert(query, [data_model.first_name, data_model.last_name, data_model.check_in_timestamp])
            if DEBUG:
                Breadcrumb.throw_crumb(INSERTED_STUDENT_DATA, _id=id)
            return _id
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(INSERT_STUDENT_FAILED)
                print(e)
            self.db.rollback()
            raise e

    def get_students(self):
        try:
            query = self.queryBuilder.build(self.queryTypes.SELECT, self.TABLE)
            result = self.get_many(query)
            if len(result) == 0:
                return list()

            fetched_cols = [desc[0] for desc in self.get_descriptions()]
            students = list()
            for data in result:
                students.append(dict(zip(fetched_cols, data)))
            return students
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(GET_STUDENTS_FAILED)
                print(e)
            raise e

    def get_student(self, data_model):
        try:
            query = self.queryBuilder.build(self.queryTypes.SELECT, self.TABLE, [self.ID_COL])
            student = self.get(query, [data_model.id])
            return student
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(GET_STUDENT_FAILED)
                print(e)
            raise e

    def delete_student(self, data_model):
        try:
            query = self.queryBuilder.build(self.queryTypes.DELETE, self.TABLE, [self.ID_COL])
            self.delete(query, [data_model.id])
        except Exception as e:
            if DEBUG:
                Breadcrumb.throw_crumb(DELETE_STUDENT_FAILED)
                print(e)
            raise e