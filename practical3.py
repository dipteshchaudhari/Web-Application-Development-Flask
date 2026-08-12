from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_page():
    return "<h1>Hello Flask</h1>"

@app.route("/home")
def home_page():
    return "<h1>This is the Home page</h1>"

@app.route("/about")
def about_page():
    return "<h1>This is the About page</h1>"

@app.route("/Contact")
def Contact_page():
    return "<h1>This is the Contact page</h1>"

@app.route("/college")
def college_page():
    return "<h1>Welcome to parul University</h1>"   

