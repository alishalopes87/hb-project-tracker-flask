"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student"""

    return render_template("student_search.html")

@app.route("/student-add")
def student_add():
    """Handles student data"""

    # first, last, github = request.form.get(["first_name","last_name","github"])
    
    return render_template("student_add.html")


@app.route("/student-confirm", methods=['POST'])
def student_confirm():
    """Confirm student add"""

    first = request.form.get("first_name")
    last = request.form.get("last_name")
    github = request.form.get("github")

    hackbright.make_new_student(first, last, github)

    return render_template("student_confirm.html",
                            first=first,
                            last=last,
                            github=github)

    

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
