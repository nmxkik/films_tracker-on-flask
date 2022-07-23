from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Post, Tag
from posts.blueprint import main_page

app.register_blueprint(main_page, url_prefix="/")

### ADMIN ###
admin = Admin(app)
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Tag, db.session))

if __name__ == "__main__":
    app.run(port=8080)
