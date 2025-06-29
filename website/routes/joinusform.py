from flask import Blueprint, request, jsonify
import pandas as pd
import os
import uuid
from datetime import datetime

joinusform = Blueprint('joinusform', __name__)

UPLOAD_FOLDER = 'uploads'
DATA_FOLDER = 'data'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DATA_FOLDER, exist_ok=True)

@joinusform.route('/submit-joinus', methods=['POST'])
def submit_joinus():
    name = request.form.get('name')
    email = request.form.get('email')
    mobile = request.form.get('mobile')
    category = request.form.get('category')
    file = request.files.get('file')
    submission_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # Save uploaded file with unique name  
    if file and file.filename != '':  
        unique_filename = f"{uuid.uuid4().hex}_{file.filename}"  
        file_path = os.path.join(UPLOAD_FOLDER, unique_filename)  
        file.save(file_path)  
    else:  
        unique_filename = ''  

    # Append form data to CSV  
    data = {  
        "Name": [name],  
        "Email": [email],  
        "Mobile": [mobile],  
        "Category": [category],  
        "Filename": [unique_filename],
        "Datetime": [submission_time] 
    }  

    csv_path = os.path.join(DATA_FOLDER, 'joinus.csv')  
    if os.path.exists(csv_path):  
        df = pd.read_csv(csv_path)  
        new_df = pd.DataFrame(data)  
        combined_df = pd.concat([df, new_df], ignore_index=True)  
        combined_df.to_csv(csv_path, index=False)  
    else:  
        pd.DataFrame(data).to_csv(csv_path, index=False)  

    return jsonify({'success': True})
