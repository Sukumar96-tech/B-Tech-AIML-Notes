
from database import db


class Year(db.Model):
    __tablename__ = "years"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    subjects = db.relationship(
        "Subject",
        backref="year",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Year {self.name}>"


class Subject(db.Model):
    __tablename__ = "subjects"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    year_id = db.Column(
        db.Integer,
        db.ForeignKey("years.id"),
        nullable=False
    )

    notes = db.relationship(
        "Note",
        backref="subject",
        lazy=True,
        cascade="all, delete"
    )

    def __repr__(self):
        return f"<Subject {self.name}>"


class Note(db.Model):
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(100), nullable=False)

    drive_link = db.Column(db.Text)

    download_link = db.Column(db.Text)

    subject_id = db.Column(
        db.Integer,
        db.ForeignKey("subjects.id"),
        nullable=False
    )

    def __repr__(self):
        return f"<Note {self.title}>"

