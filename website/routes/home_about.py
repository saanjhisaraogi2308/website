from flask import Blueprint, render_template

home_about = Blueprint('home_about', __name__)

@home_about.route('/home_about')
def home_about_page():
    return render_template('home_about.html')
