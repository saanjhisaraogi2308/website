from flask import Blueprint, render_template

termsandconditions = Blueprint('termsandconditions', __name__)

@termsandconditions.route('/termsandconditions')
def termsandconditons_page():
    return render_template('termsandconditions.html')
