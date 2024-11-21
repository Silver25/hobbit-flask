import os
from flask import Flask, render_template


app = Flask(__name__)   # 2 blank lines separate each function to keep it PEP8 compliant


@app.route("/")   # decorator
def index():
    return render_template("index.html")   # return the HTML template


@app.route("/about")
def about():
    return render_template("about.html", page_title="About", list_of_numbers=[1, 2, 3])   # return the HTML template, and insert Heading in <H2> tags


@app.route("/contact")
def contact():
    return render_template("contact.html", page_title="Contact")   # return the HTML template, and insert Heading in <H2> tags


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")   # return the HTML template, and insert Heading in <H2> tags


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)