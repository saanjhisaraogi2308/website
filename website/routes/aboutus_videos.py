from flask import Blueprint, render_template

aboutus_videos = Blueprint('aboutus_videos', __name__)

@aboutus_videos.route('/aboutus_videos')
def aboutus_videos_page():
    return render_template('aboutus_videos.html')
