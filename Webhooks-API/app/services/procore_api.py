# app/services/procore_api.py

import requests

def get_procore_data():
    # Example function to interact with Procore API
    url = 'https://api.procore.com/vapid/projects'
    headers = {
        'Authorization': 'Bearer YOUR_ACCESS_TOKEN',
    }
    response = requests.get(url, headers=headers)
    return response.json()  # Return the API response as JSON
