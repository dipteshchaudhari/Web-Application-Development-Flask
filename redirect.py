from flask import Flask,redirect
app = Flask(__name__)

@app.route("/old")
def old():
    return redirect("/new")

@app.route("/new")
def new():
    return "You're redirected to the new URL"