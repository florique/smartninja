from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/impressum")
def impressum():
    return render_template("impressum.html")


if __name__ == "__main__":
    app.debug = False
    app.run()
