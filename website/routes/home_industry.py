from flask import Blueprint, render_template

home_industry = Blueprint('home_industry', __name__)

@home_industry.route('/home_industry')
def home_industry_page():
    return render_template('home_industry.html')
