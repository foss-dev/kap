from flask import Blueprint, jsonify, request


from tracer.data.models import db, Languages

language = Blueprint('languages', __name__)

@language.route('/', methods=['GET'])
def all_list():

    results = []

    languages = Languages.query.with_entities(Languages.id, Languages.name, Languages.logo_path).all()

    for lang in languages:

        results.append({
            "id": lang.id,
            "name": lang.name,
            "logo_path": lang.logo_path
        })

    return jsonify(results)

@language.route('/', methods=['POST'])
def create_language():

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't add language"
    }

    name = request.form['name']
    logo_path = None

    try:
        logo_path = request.form['logo_path']
    except Exception:
        pass

    new_language = Languages(name, logo_path)
    db.session.add(new_language)

    try:

        db.session.commit()

        if new_language.id > 0:
            status = {
                "id": new_language.id,
                "success": True,
                "message": "Language added successfully"
            }

    except Exception:

        db.session.rollback()
        status['message'] = "Unexpected error"


    return jsonify(status)

@language.route('/<int:id>', methods=['PUT'])
def update_user(id):
    
    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't update language"
    }

    name = request.json['name']
    logo_path = None

    try:
        logo_path = request.json['logo_path']
    except Exception:
        pass

    new_language = Languages.query.filter_by(id=id).first()

    try:
        
        new_language.name = name
        new_language.logo_path = logo_path

        db.session.commit()

        status['id'] = id
        status['success'] = True
        status['message'] = "Language updated successfully"

    except AttributeError:

        db.session.rollback()
        status['message'] = "Language couldn't find"

    return jsonify(status)