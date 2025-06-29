from flask import Blueprint, render_template

aboutus_milestones = Blueprint('aboutus_milestones', __name__)

@aboutus_milestones.route('/aboutus_milestones')
def aboutus_milestones_page():
    return render_template('aboutus_milestones.html')