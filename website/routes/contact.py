from flask import Blueprint, request, redirect, url_for, flash
from datetime import datetime

contact = Blueprint('contact', __name__)

@contact.route('/submit_enquiry', methods=['POST'])
def submit_enquiry():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    message = request.form.get('message')
    category = request.form.get('category') or 'Uncategorized'
    submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Basic validation (you can add more)
    if not (name and email and mobile):
        flash('Please fill all required fields.', 'error')
        return redirect(url_for('home.homepage'))  # or wherever the form is

    # Save data logic here (e.g. write to CSV, DB etc)
    save_enquiry_to_csv(name, email, mobile, message, category, submission_time)

    # flash('Thank you for your enquiry! We will get back to you soon.', 'success')
    return redirect(url_for('home.homepage', submitted='true'))

import csv
import os

def save_enquiry_to_csv(name, email, mobile, message, category, submission_time):
    file_path = os.path.join('data', 'enquiries.csv')
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write header if file doesn't exist yet
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Mobile', 'Message', 'Category', 'submission_time'])
        writer.writerow([name, email, mobile, message, category, submission_time])
