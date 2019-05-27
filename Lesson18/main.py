from flask import Flask, render_template, request, redirect, url_for, make_response
from Lesson18.User import User
app = Flask(__name__)

@app.route("/")
def index():
        email_address = request.cookies.get("user_mail")

        if email_address:
            user = User.fetch_one(query=["mail", "==", email_address])
        else:
            user = none

        return render_template("index.html", user=user)

@app.route("/login", methods=["POST"])
def login():
    # request.
    user_name = request.form.get("user-name")
    user_mail = request.form.get("user-email")

    user = User(name=user_name, mail=user_mail)
    user.create()

    response = make_response(redirect(url_for("index")))
    response.set_cookie("user_mail", user_mail)

    return response

@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("index")))
    response.set_cookie("user_mail", expires=0)

    return response

if __name__ == "__main__":
    app.run()