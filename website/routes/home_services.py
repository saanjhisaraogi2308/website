from flask import Blueprint, render_template

home_services = Blueprint('home_services', __name__)

@home_services.route('/home_services')
def home_services_page():
    return render_template('home_services.html')
