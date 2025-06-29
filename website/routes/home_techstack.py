from flask import Blueprint, render_template

home_techstack = Blueprint('home_techstack', __name__)

@home_techstack.route('/home_techstack')
def home_techstack_page():
    return render_template('home_techstack.html')
