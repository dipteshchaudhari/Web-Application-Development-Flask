from flask import Flask,request

app = Flask(__name__)

# Example 1 [get method]

@app.route("/hello",methods=["GET"])
def hello():

    name = request.args.get("name")

    return f"Hello, {name}!"


# Example 2 :Searching For a Student [get method]

@app.route("/student")
def student():

    name = request.args.get("name")

    return f"Searching for student : {name}"
