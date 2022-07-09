from turtle import title
from flask import Blueprint, render_template
from flask import request
from flask import redirect
from flask import url_for

from app import app, db
from models import Post
from .forms import PostForm


main_page = Blueprint("main", __name__, template_folder="templates")

@app.route("/admin/create", methods=['GET', 'POST'])
def create_post():
    
    if request.method == "POST":
        title = request.form["title"]
        cardtitle = request.form["cardtitle"]
        image = request.form["image"]
        country = request.form["country"]
        release_date = request.form["release_date"]
        genre = request.form["genre"]
        cast_actors = request.form["cast_actors"]
        rating = request.form["rating"]
        description = request.form["description"]
        
        try:
            post = Post(
                title=title, 
                cardtitle=cardtitle, 
                img=image, 
                country=country, 
                release_date=release_date, 
                genre=genre, 
                cast_actors=cast_actors, 
                rating=rating, 
                description=description
            )
            db.session.add(post)
            db.session.commit()
        except:
            print("Something wrong")
        return redirect( url_for("index"))
    else:
        form = PostForm()
        return render_template("admin/create_post.html", form=form)
    

@app.route("/")
def index():
    query = request.args.get("query")
    if query:
        posts = Post.query.filter(Post.title.contains(query))
    else:
        posts = Post.query.all()
    
    return render_template("main/index.html", posts=posts)

