#stores standard routes for the website (home, etc)

from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/') #defines a view in flask, when we type in '/' whatever is in that route will call home
@login_required #decorator that does not allow a user to see the home page unless they are logged in
def home():
    return render_template("home.html")
