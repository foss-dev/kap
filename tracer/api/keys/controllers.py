from flask import Blueprint, jsonify, request

from tracer.data.models import db, Keys
from tracer.utils.key_generator import generate_key

keys = Blueprint('keys', __name__)

@keys.route("/generate", methods=['POST'])
def generate():

    user_id = request.form['user_id']
    application_id = request.form['application_id']

    key_obj = {
        "user_id": user_id,
        "application_id": application_id
    }

    generated_key = generate_key(key_obj)

    key = Keys(user_id, application_id, generated_key, True)

    db.session.add(key)
    db.session.commit()

    output = {
        "user_id": user_id,
        "application_id": application_id,
        "key": generated_key,
        "key_id": key.id
    }

    return jsonify(output)