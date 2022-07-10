from flask import Blueprint, redirect, render_template, request, url_for
from models import Post

from app import app, db

from .forms import PostForm

main_page = Blueprint("main", __name__, template_folder="templates")


@app.route("/admin/create", methods=["GET", "POST"])
def create_post():

    if request.method == "POST":
        try:
            post = Post(
                title=request.form["title"],
                cardtitle=request.form["cardtitle"],
                img=request.form["image"],
                country=request.form["country"],
                release_date=request.form["release_date"],
                genre=request.form["genre"],
                cast_actors=request.form["cast_actors"],
                rating=request.form["rating"],
                description=request.form["description"],
            )
            db.session.add(post)
            db.session.commit()
        # trunk-ignore(flake8/E722)
        except:
            print("Something wrong")
        return redirect(url_for("index"))
    else:
        form = PostForm()
        return render_template("admin/create_post.html", form=form)


@app.route("/")
def index():
    query = request.args.get("query")

    page = request.args.get("page")

    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if query:
        posts = Post.query.filter(Post.title.contains(query))
    else:
        #        posts = Post.query.all()
        posts = Post.query.order_by(Post.rating.desc())
        last_posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=1)

    return render_template(
        "main/index.html", last_posts=last_posts, pages=pages
    )
