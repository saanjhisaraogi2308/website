from flask import Blueprint, render_template

privacy = Blueprint('privacy', __name__)

@privacy.route('/privacy')
def privacy_page():
    return render_template('privacy.html')
