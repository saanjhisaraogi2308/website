from flask import Blueprint, request, jsonify
import os
import csv
import re

chatbot = Blueprint('chatbot', __name__)
chat_state = {}

@chatbot.route('/message', methods=['POST'])
def chat():
    user_input = request.get_json().get('message', '').strip()
    session_id = request.remote_addr or 'anonymous'
    state = chat_state.get(session_id, {'step': 0, 'responses': []})

    steps = [
        'Hi there! What is your name?',
        'Please enter your email address.',
        'Please provide your contact number.',
        'What question would you like to ask us?'
    ]

    if state['step'] > 0:
        if not validate_input(state['step'] - 1, user_input):
            return jsonify({'reply': validation_message(state['step'] - 1), 'finished': False})
        state['responses'].append(user_input)

    if state['step'] < len(steps):
        reply = steps[state['step']]
        state['step'] += 1
        chat_state[session_id] = state
        return jsonify({'reply': reply, 'finished': False})
    else:
        if len(state['responses']) == len(steps):
            save_to_csv(state['responses'])
        reply = "✅ Thank you! Our team will reach out to you shortly."
        chat_state.pop(session_id, None)
        return jsonify({'reply': reply, 'finished': True})

def validate_input(step, value):
    if step == 0:
        return len(value) >= 3 and value.replace(' ', '').isalpha()
    elif step == 1:
        return re.match(r'^[^\s@]+@[^\s@]+\.[^\s@]+$', value)
    elif step == 2:
        return re.match(r'^\d{10}$', value)
    elif step == 3:
        return len(value) >= 3
    return True

def validation_message(step):
    if step == 0:
        return "⚠️ Please enter a valid name (only letters, min 3 characters)."
    elif step == 1:
        return "⚠️ Please enter a valid email address."
    elif step == 2:
        return "⚠️ Please enter a valid 10-digit contact number."
    elif step == 3:
        return "⚠️ Please describe your question briefly."
    return "⚠️ Invalid input."

def save_to_csv(data):
    folder = os.path.join(os.getcwd(), 'data')
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, 'chatbot_leads.csv')
    file_exists = os.path.isfile(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'Email', 'Contact Number', 'Question'])
        writer.writerow(data)
