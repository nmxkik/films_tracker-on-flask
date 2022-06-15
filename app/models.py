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
    slug = db.Column(db.String(140), unique=True)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    
    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()
        
    def generate_slug(self):
        if self.title:
            self.slug = str(self.id) + slugify(self.title)
            
    def __repr__(self) -> str:
        return "<post id: {}, title: {}>".format(self.id, self.title)