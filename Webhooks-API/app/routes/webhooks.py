# app/routes/webhooks.py

from flask import Blueprint, request, jsonify

# Create a Blueprint for webhooks
webhooks_bp = Blueprint('webhooks', __name__)

@webhooks_bp.route('/webhook', methods=['POST'])
def handle_webhook():
    # Handle webhook data
    data = request.get_json()
    # Process the incoming data (e.g., save to the database)
    return jsonify({'status': 'success', 'data': data}), 200
