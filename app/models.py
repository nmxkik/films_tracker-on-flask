from app import db
from sqlalchemy import Column, Integer
from datetime import datetime
import re



def slugify(s):
    pattern = r'[^\w+]'
    format_str = re.sub(pattern, '-', s).lower()
    while '--' in format_str:
        format_str = format_str.replace('--', '-')
    return format_str
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
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
        
    def generate_slug(self):
        if self.title:
            self.slug = str(self.id) + slugify(self.title)
            
    def __repr__(self):
        return "<post id: {}, title: {}>".format(self.id, self.title)
    
    
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))
    
    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return "<Tag id: {}, genre: {}>".format(self.id, self.name)