from flask import Blueprint, render_template

aboutus_certifications = Blueprint('aboutus_certifications', __name__)

@aboutus_certifications.route('/aboutus_certifications')
def aboutus_certifications_page():
    return render_template('aboutus_certifications.html')
