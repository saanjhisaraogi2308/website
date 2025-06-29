from flask import Blueprint, render_template

aboutus = Blueprint('aboutus', __name__)

@aboutus.route('/aboutus')
def aboutus_page():
    return render_template('aboutus.html')

