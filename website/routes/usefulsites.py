from flask import Blueprint, render_template

usefulsites = Blueprint('usefulsites', __name__)

@usefulsites.route('/usefulsites')
def usefulsites_page():
    return render_template('usefulsites.html')

