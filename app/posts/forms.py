import re
from urllib.parse import urljoin, urlparse
from flask import redirect, request, url_for
from flask_wtf import FlaskForm
import wtforms.validators as wtfv
import wtforms
from wtforms import FloatField, Form, StringField, TextAreaField, HiddenField, validators, PasswordField


class CreatePostForm(Form):
    title = StringField("title")
    cardtitle = StringField("cardtitle")
    image = StringField("image")  # FileField(validators=[FileRequired()])
    country = StringField("country")
    release_date = StringField("release date")
    genre = StringField("genre")
    cast_actors = StringField("actors")
    rating = FloatField("rating")
    description = TextAreaField("Description")

    def validate_image(form, field):
        if field.data:
            field.data = re.sub(r"[^a-z0-9_.-]", "_", field.data)
 
def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


class RedirectForm(FlaskForm):
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        if not self.next.data:
            self.next.data = get_redirect_target() or ''

    def redirect(self, endpoint='index', **values):
        if is_safe_url(self.next.data):
            return redirect(self.next.data)
        target = get_redirect_target()
        return redirect(target or url_for(endpoint, **values))
            
class LoginForm(RedirectForm):
    username = wtforms.StringField(validators=[wtfv.InputRequired()])
    password = StringField('Password', validators=[validators.Length(min=4, max=30)])
