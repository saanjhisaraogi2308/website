from flask import Blueprint, render_template

aboutus_ourteam = Blueprint('aboutus_ourteam', __name__)

@aboutus_ourteam.route('/aboutus_ourteam')
def aboutus_ourteam_page():
    return render_template('aboutus_ourteam.html')
