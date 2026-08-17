from flask import Flask,render_template

practice2 = Flask(__name__)

@practice2.route("/")
def hello():

    Username = 'Dipu'
    items = ['MS Dhoni','Virat Kohli','Rohit Sharma','Sachin Tendulakar']
    
    return render_template('practice.html', Username = Username, items = items)
