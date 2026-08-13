from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return "<h2>this is the Home page</h2>"

@app.route("/Contact/<int:number>")
def contect(number):
    # number = 123456789
    return f"<h2> Contact number is {number}</h2>"

@app.route("/<name>/<int:enrollment>")
def example(name,enrollment):

    students = ["Diptesh","Himang","Khushi"]
    return render_template("practice.html",name=name,enrollment=enrollment,students=students)


if __name__ == "__main__":
    app.run(debug=True)