# practice 9: database connecting 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employee.db"

db = SQLAlchemy(app)

class Employee(db.Model):
    emp_id = db.Column(db.Integer, primary_key = True)
    emp_name = db.Column(db.String(100), nullable = False)
    emp_email = db.Column(db.String(150), nullable = False)

with app.app_context():
    db.create_all()


@app.route("/add")
def add():

    Employee1 = Employee(
        emp_name = "Diptesh Chaudhary",
        emp_email = "dipteshchaudhary303@gmail.com"
    )

    db.session.add(Employee1)
    db.session.commit()

    return "employee added Successfully!!"

@app.route("/employees")
def employees():
    all_employees = Employee.query.all()

    result = " "

    for employee in all_employees:
        result += f"""
        ID : {employee.emp_id} <br>
        Name : {employee.emp_name} <br>
        Email : {employee.emp_email} <br> 
        <hr>
        """
    return result

if __name__ == "__main__":
    app.run(debug=True)

