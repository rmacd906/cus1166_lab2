# File app.py
from flask import Flask, render_template

app = Flask(__name__)

studr = ("Ryan Macdonald", 95, "Senior")
studa = ("Alex", 90, "Sophmore")
studb = ("Bob", 86, "Freshman")
studc = ("Chad", 82, "Sophmore")
studd = ("Dale", 78, "Freshman")
stude = ("Eric", 74, "Senior")
studf = ("Fred", 76, "Junior")
class_roster = [studr, studa, studb, studc, studd, stude, studf]

# Demonstrate separation of templates, basic
@app.route("/")
def index():
    return render_template("index.html")

# Separation of UI
# Example of passing parameters to the template.
@app.route("/welcome/<string:student_name>")
def welcome(student_name):
    return render_template("welcome.html", student_name=student_name)

# Example of loops in in templates.
@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", grade_view=grade_view, class_roster = class_roster)

if __name__ == "__main__":
    app.run()
