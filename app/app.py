from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager


from config import Configuration
from posts.blueprint import posts


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='templates')
app.config.from_object(Configuration)

db = SQLAlchemy(app)


migrate = Migrate(app, db)
manager = Manager(app)

