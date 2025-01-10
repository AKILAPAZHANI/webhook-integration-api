# app/routes/import.py

from flask import Blueprint, request, jsonify
from app.models import Project
from app import db

import_bp = Blueprint('import', __name__)

@import_bp.route('/import', methods=['POST'])
def import_project():
    data = request.get_json()
    # Create new Project from the data
    project = Project(name=data['name'], description=data.get('description'))
    db.session.add(project)
    db.session.commit()
    return jsonify({'status': 'success', 'project': project.name}), 200
