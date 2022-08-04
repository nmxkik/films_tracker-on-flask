from flask import Blueprint, redirect, render_template, request, url_for
from models.posts import Post

from app import app, db

from posts.forms import CreatePostForm

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
        except Exception as error:
            print(error)
            return redirect('/admin/create')
        return redirect(url_for("index"))
    else:
        form = CreatePostForm()
        return render_template("admin/create_post.html", form=form)


@app.route("/edit/<id>", methods=["POST", "GET"])
def edit_post(id):
    post = Post.query.get_or_404(id)
    print(post.id)

    if request.method == "POST":
        form = CreatePostForm(request.form, obj=post)

        if form.validate():
            form.populate_obj(post)
            #db.session.add(post)
            db.session.commit()

        return "Hello world"#redirect(url_for("posts.post_detail", slug=post.slug))

    form = CreatePostForm(obj=post)
    return render_template("admin/edit_post.html", post=post, form=form)


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
        posts = Post.query.order_by(Post.rating.desc())
        last_posts = Post.query.order_by(Post.created.desc())

    pages = posts.paginate(page=page, per_page=20)

    return render_template("main/index.html", last_posts=last_posts, pages=pages)


@app.route("/<slug>", methods=["GET"])
def get_post(slug):

    post = Post.query.filter(Post.slug == slug).first()

    return render_template("posts/post_detail.html", post=post)
