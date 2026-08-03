from flask import Flask   # importing class flask from Flask package

app = Flask(__name__)   #create flash application and tells Flask which module is creating it.

@app.route("/")         
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)