from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash 
from . import db #importing data base from __init__
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Successfully Logged In!', category = 'success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again', category = 'error')
        else:
            flash('There is no account associated with that email', category = 'error')

    return render_template("login.html", boolean=False )

@auth.route('/logout')
@login_required # you can only access this route if a user is logged in, they cant log out if they havent logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=["GET", "POST"])
def sign_up():
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        email = request.form.get('email')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        
        #checking to see if the user inputs are valid
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('An account with this email already exists, please log in or create a new account', category ='error')

        if len(email) < 4:
            flash('Email must be greater than 3 characters', category='error')
        elif len(first_name) < 2:
            flash('First name miust be greater than 1 chatacter', category='error')
        elif password1 != password2:
            flash('Passwords do not match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password = generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account Created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html")

