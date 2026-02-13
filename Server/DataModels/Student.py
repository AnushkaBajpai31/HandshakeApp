from datetime import datetime


class Student:
    def __init__(self, id=None, first_name="", last_name="", check_in_timestamp=None):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.check_in_timestamp = check_in_timestamp if check_in_timestamp is not None else datetime.now()

    def to_dict(self):
        return dict(self.__dict__)

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)