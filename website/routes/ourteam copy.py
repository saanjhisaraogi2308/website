from flask import Blueprint, render_template

ourteam = Blueprint('ourteam', __name__)

@ourteam.route('/ourteam')
def ourteam_page():
    return render_template('ourteam.html')
