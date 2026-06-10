# 📚 AIML Notes Portal

AIML Notes Portal is a Flask-based web application that helps students easily access study materials such as notes, PDFs, and Google Drive resources. The application also includes an Admin Panel for managing Years, Subjects, and Notes.

---

# 🚀 Features

## 👨‍🎓 Student Module

* View available academic years
* View subjects based on the selected year
* Access notes for each subject
* Download PDF notes
* Open Google Drive resources

---

## 👨‍💼 Admin Module

* Secure Admin Login
* Admin Dashboard
* Add Year
* View Years
* Add Subject
* View Subjects
* Add Notes
* View Notes
* Delete records
* Session-based authentication

---

# 🛠️ Tech Stack

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* Neon PostgreSQL

### Tools

* Git
* GitHub
* VS Code

---

# 📁 Project Structure

```
AIML_Notes/

│
├── app.py
├── config.py
├── database.py
├── models.py
├── requirements.txt
├── .env
│
├── routes/
│     ├── __init__.py
│     ├── student.py
│     └── admin.py
│
├── templates/
│     ├── base.html
│     ├── index.html
│     ├── subjects.html
│     ├── notes.html
│     ├── admin_login.html
│     ├── admin_dashboard.html
│     ├── add_year.html
│     ├── add_subject.html
│     ├── add_note.html
│
├── static/
│     ├── css/
│     ├── js/
│     └── images/
```

---

# ⚙️ Installation

## Clone the repository

```bash
git clone https://github.com/your-username/AIML_Notes.git
```

## Navigate to the project

```bash
cd AIML_Notes
```

## Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

---

## Install dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```
DATABASE_URL=your_neon_database_url
SECRET_KEY=your_secret_key
```

---

## Run the application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

# 🗄️ Database Schema

## Year

* id
* name

## Subject

* id
* name
* year_id

## Note

* id
* title
* drive_link
* download_link
* subject_id

---

# 📌 Application Flow

```
Student

Home
   │
   ▼
Select Year
   │
   ▼
Select Subject
   │
   ▼
View Notes
   │
   ├── Download PDF
   └── Open Drive


Admin

Login
   │
   ▼
Dashboard
   │
   ├── Add Year
   ├── Add Subject
   ├── Add Note
   ├── View Years
   ├── View Subjects
   └── View Notes
```

---

# 🔮 Future Enhancements

* Edit Year
* Edit Subject
* Edit Notes
* Search functionality
* PDF upload support
* Student authentication
* Responsive mobile UI
* Role-based access control
* Deployment on Render

---

# 👨‍💻 Author

**Sukumar**

Artificial Intelligence & Machine Learning Student

Passionate about Python, Flask, Data Analytics, Machine Learning, and Full Stack Development.

---

# ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
