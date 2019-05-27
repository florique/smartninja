from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    page_title = "Homepage"

    cities = ["Wien", "Prag", "Bratislava", "London"]

    return render_template("index.html", page_title=page_title, cities=cities)

if request.method == "GET":
    user_name = request.cookies.get("user_name")
    return render_template("about.html", name=user_name)


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")

@app.route("/about")
def about():


    return render_template("about.html")

@app.route("/contact", methods=["POST"])
def success():
    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_message = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_message)

    response = make_response(render_template("success.html"))
    response.set_cookie("user_name", contact_name)

    return response

if __name__ == "__main__":
    app.debug = False
    app.run()
