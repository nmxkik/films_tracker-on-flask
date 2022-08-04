from flask import Blueprint, render_template, request, session, jsonify
from werkzeug.security import check_password_hash

from app import app, login_manager
from account.forms import LoginForm
from models.user import User


login_page = Blueprint('login', __name__, static_folder='static', static_url_path='/static/login')

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        if form.validate_on_submit():
            return form.redirect('index')
        return render_template('main/Login.html', form=form)

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = User.query.filter(User.login == username).one()
        if result:
            rs_password = result.password
            if check_password_hash(rs_password, password):
                session['logged_in'] = True
                session['username'] = username
                msg = 'success'
            else:
               msg = 'No-data'
        else:
            msg = 'No-data'   
    return jsonify(msg)   

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    pass