import os
from flask import Flask, render_template


app = Flask(__name__)   # 2 blank lines separate each function to keep it PEP8 compliant


@app.route("/")   # decorator
def index():
    return render_template("index.html")   # return the HTML template


@app.route("/about")
def about():
    return render_template("about.html")   # return the HTML template


@app.route("/contact")
def contact():
    return render_template("contact.html")   # return the HTML template


@app.route("/careers")
def careers():
    return render_template("careers.html")   # return the HTML template


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)