from flask import Blueprint, jsonify, request


from tracer.data.models import db, Applications

applications = Blueprint('applications', __name__)

@applications.route('/<int:id>', methods=['GET'])
def application_details(id):

    application_object = {
        "error": "Application not found"
    }

    application = Applications.query \
                .with_entities(Applications.id, Applications.active, Applications.created_at, 
                Applications.updated_at, Applications.title, Applications.description, Applications.repo, Applications.user_id) \
                .filter(Applications.id == id).first()
    
    if application:

        application_object = {
            "id": application.id,
            "active": application.active,
            "created_at": application.created_at.strftime("%d.%m.%Y %H:%M:%S"),
            "updated_at": application.updated_at.strftime("%d.%m.%Y %H:%M:%S") if application.updated_at else None,
            "title": application.title,
            "description": application.description,
            "repo": application.repo,
            "user_id": application.user_id
        }

    return jsonify(application_object)

@applications.route('/', methods=['POST'])
def create():

    user_id = request.form["user_id"]
    title = request.form["title"]
    description = request.form["description"]
    repo = request.form["repo"]
    active = True if request.form['active'] == 'true' else False

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't add application"
    }

    application = Applications(user_id, title, description, repo, active)

    db.session.add(application)

    db.session.commit()

    if application.id > 0:
        status["id"] = application.id
        status["success"] = True
        status["message"] = "Application added successfully"

    return jsonify(status)


@applications.route('/<int:id>', methods=['PUT'])
def update(id):

    user_id = request.json["user_id"]
    title = request.json["title"]
    description = request.json["description"]
    repo = request.json["repo"]
    active = request.json['active']

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't update application"
    }

    application = Applications.query.filter_by(id=id).first()

    db.session.commit()

    try:

        application.user_id = user_id
        application.title = title
        application.description = description
        application.repo = repo
        application.active = active

        db.session.commit()
        status["id"] = id
        status["success"] = True
        status["message"] = "Application updated successfully"

    except AttributeError:
        
        db.session.rollback()
        status['message'] = "Application couldn't find"

    return jsonify(status)


@applications.route('/<int:id>', methods=['DELETE'])
def delete(id):

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't delete application"
    }

    application = Applications.query.filter_by(id=id).first()

    try:

        db.session.delete(application)
        db.session.commit()

        status["id"] = id
        status["success"] = True
        status["message"] = "Application deleted successfully"

    except Exception:
        
        db.session.rollback()

        status["message"] = "Application couldn't find."
    
    return jsonify(status)