from flask import Blueprint, render_template

home_ourclients = Blueprint('home_ourclients', __name__)

@home_ourclients.route('/home_ourclients')
def ourclients_page():
    return render_template('home_ourclients.html')
