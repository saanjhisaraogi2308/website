from flask import Blueprint, render_template

faq = Blueprint('faq', __name__)

@faq.route('/faq')
def faq_page():
    return render_template('faq.html')
