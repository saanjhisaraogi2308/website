from flask import Blueprint, render_template

home_why = Blueprint('home_why', __name__)

@home_why.route('/home_why')
def home_why_page():
    return render_template('home_why.html')