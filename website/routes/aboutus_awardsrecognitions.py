from flask import Blueprint, render_template

aboutus_awardsrecognitions = Blueprint('aboutus_awardsrecognitions', __name__)

@aboutus_awardsrecognitions.route('/aboutus_awardsrecognitions')
def aboutus_awardsrecognitions_page():
    return render_template('aboutus_awardsrecognitions.html')
