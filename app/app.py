from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from flask_wtf import CSRFProtect


from config import Configuration


main_page = Blueprint("main", __name__, template_folder="templates")



app = Flask(
    __name__, static_url_path="", static_folder="static", template_folder="templates"
)
app.config.from_object(Configuration)



db = SQLAlchemy(app)

#csrf = CSRFProtect(app)
#csrf.init_app(app)






migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)



