from flask import Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy

from config import Configuration


app = Flask(
    __name__, static_url_path="", static_folder="static", template_folder="templates"
)
app.config.from_object(Configuration)

db = SQLAlchemy(app)


migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)

