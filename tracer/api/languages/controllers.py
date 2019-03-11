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