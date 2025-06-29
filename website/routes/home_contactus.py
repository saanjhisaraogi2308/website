from flask import Blueprint, render_template

home_contactus = Blueprint('home_contactus', __name__)

@home_contactus.route('/home_contactus')
def contactus_page():
    return render_template('home_contactus.html')
