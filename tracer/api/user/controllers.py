from flask import Blueprint, jsonify, request
from werkzeug import generate_password_hash
from sqlalchemy.exc import IntegrityError

from tracer.data.models import db, User, Role

user = Blueprint('user', __name__)

@user.route('/', methods=['GET'])
def get_users():
    
    users = User.query \
        .with_entities(User.id, User.active, User.email, User.name, Role.id.label('roleid'), Role.name.label('rolename')) \
        .join(Role, Role.id == User.roles) \
        .all()
    
    user_list = []
    
    for user in users:
        user_list.append({
            "id": user.id,
            "active": user.active,
            "email": user.email,
            "name": user.name,
            "role_id": user.roleid,
            "role_name": user.rolename
        })

    return jsonify(user_list)

@user.route('/<int:id>', methods=['GET'])
def user_info(id):

    user = User.query \
        .with_entities(User.id, User.active, User.email, User.name, Role.id.label('roleid'), Role.name.label('rolename')) \
        .join(Role, Role.id == User.roles) \
        .filter(User.id == id).first()
    
    user_object = {
        "error": "User Not Found"
    }
    
    if user:
        user_object = {
            "id": user.id,
            "active": user.active,
            "email": user.email,
            "name": user.name,
            "role_id": user.roleid,
            "role_name": user.rolename
        }

    return jsonify(user_object)

@user.route('/', methods=['POST'])
def create_user():

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't add user"
    }

    email = request.form['email']
    name = request.form['name']
    password = generate_password_hash(request.form['password'])
    active = True if request.form['active'] == 'true' else False
    roles = request.form['roles']

    user = User(email, name, password, active, roles)
    db.session.add(user)

    try:

        db.session.commit()

        if user.id > 0:
            status = {
                "id": user.id,
                "success": True,
                "message": "User added successfully"
            }

    except IntegrityError:

        db.session.rollback()
        status['message'] = "This email already exists in the system"


    return jsonify(status)


@user.route('/<int:id>', methods=['PUT'])
def update_user(id):
    
    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't update user"
    }

    email = request.json['email']
    name = request.json['name']
    password = generate_password_hash(request.json['password'])
    active = request.json['active']
    roles = request.json['roles']

    user = User.query.filter_by(id=id).first()

    try:
        
        user.email = email
        user.name = name
        user.password = password
        user.active = active
        user.roles = roles

        db.session.commit()

        status['id'] = id
        status['success'] = True
        status['message'] = "User updated successfully"

    except AttributeError:

        db.session.rollback()
        status['message'] = "User couldn't find"

    return jsonify(status)


@user.route('/<int:id>', methods=['DELETE'])
def delete_user(id):

    status = {
        "id": 0,
        "success": False,
        "message": "Error: Couldn't delete user"
    }

    user = User.query.filter_by(id=id).first()

    try:

        db.session.delete(user)
        db.session.commit()

        status["id"] = id
        status["success"] = True
        status["message"] = "User deleted successfully"

    except Exception:
        
        db.session.rollback()

        status["message"] = "User couldn't find."

    return jsonify(status)