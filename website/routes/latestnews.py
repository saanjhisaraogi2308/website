from flask import Blueprint, render_template

latestnews = Blueprint('latestnews', __name__)

@latestnews.route('/latestnews')
def latest_news_page():
    return render_template('latestnews.html')