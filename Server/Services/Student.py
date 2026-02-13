from DataAccess.Student import Student as StudentDataAccess
from Logging.Breadcrumb import Breadcrumb
from config import DEBUG
from constants import *


class Student:
    def __init__(self):
        self.student_data_access = StudentDataAccess()

    def get_students(self):
        if DEBUG:
            Breadcrumb.throw_crumb(GETTING_STUDENTS_DATA)
        response = self.student_data_access.get_students()
        for student in response:
            student[CHECK_IN_COL] = str(student.get(CHECK_IN_COL)) + UTC
        return response