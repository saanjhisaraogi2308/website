from flask import Blueprint, render_template

aboutus_gallery = Blueprint('aboutus_gallery', __name__)

@aboutus_gallery.route('/aboutus_gallery')
def aboutus_gallery_page():
    return render_template('aboutus_gallery.html')
