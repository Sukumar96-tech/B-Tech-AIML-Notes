
from flask import render_template
from app import app
from models import Year, Subject, Note


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/year/<int:year_id>")
def subjects(year_id):

    subjects = Subject.query.filter_by(
        year_id=year_id
    ).all()

    return render_template(
        "subjects.html",
        subjects=subjects
    )


@app.route("/subject/<int:subject_id>")
def notes(subject_id):

    subject = Subject.query.get_or_404(subject_id)

    notes = Note.query.filter_by(
        subject_id=subject_id
    ).all()

    return render_template(
        "notes.html",
        subject_name=subject.name,
        notes=notes
    )


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"),404