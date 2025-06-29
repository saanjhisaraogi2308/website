from flask import Blueprint, render_template

home_affiliations = Blueprint('home_affiliations', __name__)

@home_affiliations.route('/home_affiliations')
def affiliations_page():
    return render_template('home_affiliations.html')
