from posts.blueprint import main_page

from app import app

app.register_blueprint(main_page, url_prefix="/")


if __name__ == "__main__":
    app.run()
