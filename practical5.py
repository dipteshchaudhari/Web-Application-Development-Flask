from flask import Flask,render_template

app = Flask(__name__)

@app.route("/<name>/<cource>/<university>/<int:age>")
def home(name,cource,university,age):

    # name = "diptesh"
    # cource = "Msc It"
    # university = "parul"

    students = ['Diptesh','rohith','masoom']
    
    return render_template("home.html",name = name,cource = cource,university = university, age = age, students = students)