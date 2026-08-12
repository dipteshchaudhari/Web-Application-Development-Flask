from flask import Flask

prac = Flask(__name__)

@prac.route("/about/<name>")
def about_page(name):
    return f"<p>This is the About page of {name}</p>"

@prac.route("/contact/<name>/<int:number>")
def contact_page(name,number):
    return f"<h3>Contact Number of {name} is {number}</h3>"

@prac.route("/student/<name>/<cource>")
def student_page(name,cource):
    return f"<h2>Student name is {name} and he/she is in {cource}</h2>"

if __name__ == "__main__":
    prac.run(debug = True)