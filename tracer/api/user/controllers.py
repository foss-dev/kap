from flask import Blueprint, jsonify

user = Blueprint('user', __name__)

@user.route('/<int:id>')
def user_index(id):

    info = {
        "id": id,
        "username": "alişko"
    }

    return jsonify(info)

@user.route('/roles/<int:id>')
def user_roles(id):
    
    roles = {
        "user_edit": True,
        "role_delete": True
    }

    return jsonify(roles)