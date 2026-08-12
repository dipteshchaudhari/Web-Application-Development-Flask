from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")


@app.route("/submit", methods =["POST"])
def submit():
    # return "Form Submitted Successfully"
    # print(request.form)

    name = request.form["name"]
    email = request.form["email"]

    # form validation

    # if name == "":
    #     return "Name can not be Empty!"
    if not name:
        return "Name cant be Emptry!"
    if len(name) < 3:
        return "Name must contain at least 3 characters!"

    # if email == "":
    #     return "Email can not be Empty!"
    if not email:
        return "Email can't be Empty!"
    if '@' not in email:
        return "Invalid email!"
    
    return f"Name : {name} <br> Email : {email}"

if __name__ == "__main__":
    app.run(debug=True)