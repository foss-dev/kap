from flask import Blueprint, jsonify, request


from tracer.data.models import db, Keys
from tracer.utils.key_generator import generate_key

keys = Blueprint('keys', __name__)

def set_all_keys_inactive(user_id, application_id):

    keys = Keys.query.filter_by(user_id=user_id, application_id=application_id).update(dict(active=False))

    db.session.commit()


@keys.route("/generate", methods=['POST'])
def generate():

    user_id = request.form['user_id']
    application_id = request.form['application_id']

    set_all_keys_inactive(user_id, application_id)

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

@keys.route('/update/<int:id>', methods=['PUT'])
def update_key(id):

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't update key"
    }

    active = request.json["active"]

    key = Keys.query.filter_by(id=id).first()

    try:
        key.active = False

        db.session.commit()

        status['id'] = id
        status['success'] = True
        status['message'] = "Key updated successfully"

    except AttributeError:

        db.session.rollback()
        status['message'] = "Key couldn't find"

    return jsonify(status)

@keys.route('/<int:user_id>/<int:app_id>', methods=['GET'])
def key_info(user_id, app_id):

    results = Keys.query \
        .with_entities(Keys.id, Keys.application_id, Keys.user_id, Keys.active, Keys.created_at, Keys.updated_at, Keys.key) \
        .filter(Keys.application_id == app_id, Keys.user_id == user_id).all()
    
    keys = []

    for result in results:

        keys.append({
            "id": result.id,
            "application_id": result.application_id,
            "user_id": result.user_id,
            "active": result.active,
            "created_at": result.created_at.strftime("%d.%m.%Y %H:%M:%S"),
            "updated_at": result.updated_at.strftime("%d.%m.%Y %H:%M:%S") if result.updated_at else None,
            "key": result.key
        })

    return jsonify(keys)