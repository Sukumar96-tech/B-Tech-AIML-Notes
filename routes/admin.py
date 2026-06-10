from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session
)

from app import app
from database import db
from models import Year, Subject, Note
from config import Config


USERNAME = Config.ADMIN_USERNAME
PASSWORD = Config.ADMIN_PASSWORD


@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        if username == USERNAME and password == PASSWORD:

            session["admin"] = True

            return redirect(
                url_for("admin_dashboard")
            )

        return "Invalid Credentials"

    return render_template(
        "admin_login.html"
    )


@app.route("/admin/dashboard")
def admin_dashboard():

    if not session.get("admin"):

        return redirect(
            url_for("admin_login")
        )

    return render_template(
        "admin_dashboard.html"
    )

@app.route("/admin/year/add", methods=["GET", "POST"])
def add_year():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    if request.method == "POST":

        name = request.form.get("name")

        existing = Year.query.filter_by(
            name=name
        ).first()

        if existing:
            return "Year already exists"

        year = Year(
            name=name
        )

        db.session.add(year)

        db.session.commit()

        return redirect(
            url_for("view_years")
        )

    return render_template(
        "add_year.html"
    )

@app.route("/admin/years")
def view_years():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    years = Year.query.order_by(
        Year.id
    ).all()

    return render_template(
        "view_years.html",
        years=years
    )

@app.route("/admin/year/delete/<int:id>")
def delete_year(id):

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    year = Year.query.get_or_404(id)

    db.session.delete(year)

    db.session.commit()

    return redirect(
        url_for("view_years")
    )


@app.route("/admin/subject/add", methods=["GET","POST"])
def add_subject():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    if request.method == "POST":

        name = request.form.get("name")
        year_id = request.form.get("year_id")

        existing = Subject.query.filter_by(
            name=name,
            year_id=year_id
        ).first()

        if existing:
            return "Subject already exists"

        subject = Subject(
            name=name,
            year_id=year_id
        )

        db.session.add(subject)
        db.session.commit()

        return redirect(
            url_for("view_subjects")
        )

    years = Year.query.order_by(
        Year.id
    ).all()

    return render_template(
        "add_subject.html",
        years=years
    )

@app.route("/admin/subjects")
def view_subjects():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    subjects = Subject.query.order_by(
        Subject.id
    ).all()

    return render_template(
        "view_subjects.html",
        subjects=subjects
    )

@app.route("/admin/subject/delete/<int:id>")
def delete_subject(id):

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    subject = Subject.query.get_or_404(id)

    db.session.delete(subject)

    db.session.commit()

    return redirect(
        url_for("view_subjects")
    )

@app.route("/admin/note/add", methods=["GET","POST"])
def add_note():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    if request.method=="POST":

        title=request.form.get("title")
        drive_link=request.form.get("drive_link")
        download_link=request.form.get("download_link")
        subject_id=request.form.get("subject_id")

        note=Note(
            title=title,
            drive_link=drive_link,
            download_link=download_link,
            subject_id=subject_id
        )

        db.session.add(note)
        db.session.commit()

        return redirect(url_for("view_notes"))

    subjects=Subject.query.order_by(
        Subject.name
    ).all()

    return render_template(
        "add_note.html",
        subjects=subjects
    )
@app.route("/admin/notes")
def view_notes():

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    notes=Note.query.order_by(
        Note.id
    ).all()

    return render_template(
        "view_notes.html",
        notes=notes
    )
@app.route("/admin/note/delete/<int:id>")
def delete_note(id):

    if not session.get("admin"):
        return redirect(url_for("admin_login"))

    note=Note.query.get_or_404(id)

    db.session.delete(note)

    db.session.commit()

    return redirect(
        url_for("view_notes")
    )


@app.route("/admin/logout")
def logout():

    session.clear()

    return redirect(
        url_for("admin_login")
    )