from flask import Blueprint, render_template

resourcehub = Blueprint('resourcehub', __name__)

@resourcehub.route('/resourcehub')
def resourcehub_page():
    return render_template('resourcehub.html')