from flask import Blueprint, render_template

home_visionmission = Blueprint('home_visionmission', __name__)

@home_visionmission.route('/home_visionmission')
def home_visonmission_page():
    return render_template('home_visionmission.html')
