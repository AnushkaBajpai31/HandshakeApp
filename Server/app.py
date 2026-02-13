from flask import Flask
from Services.Student import Student as StudentService
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index')
def get_students_data():
    return StudentService().get_students()



if __name__ == '__main__':
    app.run()
