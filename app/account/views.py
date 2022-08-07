from flask import Blueprint, flash, redirect, render_template, request, session, jsonify, url_for
from flask_login import LoginManager, login_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
import flask_login


from app import app, db
from account.forms import LoginForm, RegistrationForm
from models.user import User


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'basic'
login_manager.login_view = 'account.login'



login_page = Blueprint('login', __name__, static_folder='static', static_url_path='/static/login')

@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None
    



@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        print(user.verify_password(password=form.password.data))
        if user and user.verify_password(password=form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        flash('Invalid username/password combination')
        return redirect(url_for('login'))
    return render_template('main/login.html', form=form)
    
    
    
    
    

    #if request.method == 'GET':
    #    form = LoginForm()
    #    if form.validate_on_submit():
    #        return form.redirect('index')
    #    return render_template('main/login.html', form=form)
#
    #if request.method == 'POST':
    #    username = request.form['username']
    #    password = request.form['password']
    #    user = User.query.filter(User.login == username).first()
    #    #print(user.id)
    #    print(password,  "1")
    #    if user:
    #        rs_password = user.password
    #        #print(rs_password, "2")
    #        #print(password,  "2")
    #        if check_password_hash(rs_password, password):
    #            session['logged_in'] = True
    #            session['username'] = username
    #            try:
    #                login_user(user)
    #            except AttributeError:
    #                print('in the except')
    #                form = LoginForm()
    #                return render_template('main/login.html', form=form)
    #                        
    #        else:
    #           msg = 'No-data'
    #    else:
    #        msg = 'No-data'   
    #return jsonify(msg)   

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    flask_login.logout_user()
    return 'Logged out'

@app.route('/registration', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print(form.data)
    if request.method == 'POST' and form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            user=User(
                email=request.form["email"], 
                login=request.form["login"], 
                )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('login'))
    return render_template('main/registration.html', form=form)