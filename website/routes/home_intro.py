from flask import Blueprint, render_template

home_intro = Blueprint('home_intro', __name__)

@home_intro.route('/home_intro')
def intro_page():
    return render_template('home_intro.html')
