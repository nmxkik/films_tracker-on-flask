import re
from datetime import datetime

from app import db


def slugify(s):
    pattern = r"[^\w+]"
    format_str = re.sub(pattern, "-", s).lower()
    while "--" in format_str:
        format_str = format_str.replace("--", "-")
    return format_str


post_tags = db.Table(
    "post_tags",
    db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
    db.Column("tag_id", db.Integer, db.ForeignKey("tag.id")),
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140))
    cardtitle = db.Column(db.String(140))
    img = db.Column(db.String(280))
    slug = db.Column(db.String(140), unique=True)
    country = db.Column(db.String(140))
    release_date = db.Column(db.String(140))
    genre = db.Column(db.String(140))
    cast_actors = db.Column(db.String(140))
    rating = db.Column(db.Float, primary_key=True)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship(
        "Tag", secondary=post_tags, backref=db.backref("posts", lazy="dynamic")
    )

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return "<post id: {}, title: {}>".format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return "<Tag id: {}, genre: {}>".format(self.id, self.name)
