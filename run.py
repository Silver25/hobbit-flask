import os
import json   # library, for passing the data that's coming in as JSON
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env


#  2 blank lines separate each function to keep it PEP8 compliant
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")   # route decorator and view
def index():
    return render_template("index.html")   # return the HTML template


# return [create] the HTML template, and insert Heading in <H2> tags
@app.route("/about")
def about():
    # initialize an empty array for Python to be able to open the JSON file
    data = []
    # opening company.json file for read-only access
    with open("data/company.json", "r") as json_data:  # "r" for Read only
        # creating another variable inside, to pass the data that ...
        # ... are pulled through and converted into JSON
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


# return the specific HTML template for specific member which url is clicked
# angle brackets will pass in data from the URL path, into view below
@app.route("/about/<member_name>")
# taking member_name from above, as an argument
def about_member(member_name):
    member = {}   # empty object to use to store data in later
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        # iterate through that data array that is just created
        for obj in data:
            # checking if that object's url key from the file is equal
            # to the member_name passed through from the URL path
            if obj["url"] == member_name:
                # If they do match, then empty 'member' object will be
                # equal to the object in this loop instance
                member = obj
    return render_template("member.html", member=member)


# to start handling anything other than GET, such as POST, DELETE or PUT,
# then we need to explicitly state that our route can accept those methods
@app.route("/contact", methods=["GET", "POST"])
def contact():   # return the HTML template, and insert Heading in <H2> tags
    if request.method == "POST":
        flash("Thanks {}, we have received your msg!".format(
            request.form.get("name")))
    return render_template("contact.html", page_title="Contact")


@app.route("/summary")
def summary():   # return the HTML template, and insert Heading in <H2> tags
    return render_template("summary.html", page_title="Summary")



if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True)