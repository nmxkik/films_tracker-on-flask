from app import app, db
from posts.blueprint import main_page

import view


app.register_blueprint(main_page, url_prefix="/")


if __name__== "__main__":
    app.run()