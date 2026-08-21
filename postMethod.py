from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("form2.html")

@app.route("/submit", methods=["POST"])
def submit():

    name = request.form["name"]
    email = request.form["email"]

    return f"Name: {name}<br>Email: {email}"