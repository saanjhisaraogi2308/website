from flask import Blueprint, render_template

home_testimonials = Blueprint('home_testimonials', __name__)

@home_testimonials.route('/home_testimonials')
def home_testimonials_page():
    return render_template('home_testimonials.html')
