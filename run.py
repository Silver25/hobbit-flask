import os
import json   # import the JSON library, for passing the data that's coming in as JSON
from flask import Flask, render_template

###  2 blank lines separate each function to keep it PEP8 compliant
app = Flask(__name__)


@app.route("/")   # decorator
def index():
    return render_template("index.html")   # return the HTML template


@app.route("/about")
def about():   # return the HTML template, and insert Heading in <H2> tags
    data = []   # initialize an empty array or list for Python to be able to open the JSON file in order to read it
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/contact")
def contact():   # return the HTML template, and insert Heading in <H2> tags
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():   # return the HTML template, and insert Heading in <H2> tags
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)