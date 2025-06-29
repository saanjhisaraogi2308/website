from flask import Blueprint, render_template

joinus = Blueprint('joinus', __name__)

@joinus.route('/joinus')
def joinus_page():
    return render_template('joinus.html')
