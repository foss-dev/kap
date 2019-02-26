from flask import Blueprint, jsonify

admin = Blueprint('admin', __name__)

@admin.route('/<int:id>')
def admin_index(id):

    info = {
        "id": id,
        "username": "alişko"
    }

    return jsonify(info)