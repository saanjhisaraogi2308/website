from flask import Blueprint, render_template

home_keystats = Blueprint('home_keystats', __name__)

@home_keystats.route('/home_keystats')
def home_keystats_page():
    return render_template('home_keystats.html')
