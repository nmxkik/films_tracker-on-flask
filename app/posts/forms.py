from wtforms import Form, StringField, FloatField,TextAreaField, FileField
from flask_wtf.file import FileRequired
import re


class PostForm(Form):
    title = StringField("title")
    cardtitle = StringField("cardtitle")
    image = StringField("image")    #FileField(validators=[FileRequired()])
    country = StringField("country")
    release_date = StringField("release date")
    genre = StringField("genre")
    cast_actors = StringField("actors")
    rating = FloatField("rating")
    description = TextAreaField('Description')
    
    
    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r'[^a-z0-9_.-]', '_', field.data)    