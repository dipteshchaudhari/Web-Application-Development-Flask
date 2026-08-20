from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///students.db"

db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    course = db.Column(db.String(100), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return "Flask-SQLAlchemy is connected!"

@app.route("/add")
def add_student():

    student1 = Student(
        name="Diptesh",
        email="diptesh@gmail.com",
        course="MSc IT"
    )

    db.session.add(student1)
    db.session.commit()

    return "Student added successfully!"

@app.route("/students")
def students():
    all_students = Student.query.all()

    result = ""

    for student in all_students:
        result += f"""
        ID: {student.id}<br>
        Name: {student.name}<br>
        Email: {student.email}<br>
        Course: {student.course}<br>
        <hr>
        """

    return result

if __name__ == "__main__":
    app.run(debug=True)