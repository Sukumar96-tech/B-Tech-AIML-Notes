from flask import Flask
from config import Config
from database import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
from models import Year, Subject, Note

with app.app_context():
    db.create_all()

# Import routes AFTER app creation
from routes.student import *
from routes.admin import *

if __name__ == "__main__":
    app.run()