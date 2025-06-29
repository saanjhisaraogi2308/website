from flask import Blueprint, render_template

aboutus_ourfounder = Blueprint('aboutus_ourfounder', __name__)

@aboutus_ourfounder.route('/aboutus_ourfounder')
def aboutus_ourfounder_page():
    return render_template('aboutus_ourfounder.html')
