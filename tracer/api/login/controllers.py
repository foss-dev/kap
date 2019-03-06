from flask import Blueprint, jsonify, request
from werkzeug import check_password_hash, generate_password_hash
from sqlalchemy.exc import IntegrityError

from tracer.data.models import db, User

login = Blueprint('login', __name__)

@login.route('/', methods=['POST'])
def login_user():

    status = {
        "success": False,
        "id": 0,
        "email": None,
        "name": None,
        "active": False,
        "roles": None,
        "message": "E-mail or Password is not correct!"
    }

    email = request.form['email']
    password = request.form['password']

    user = User.query.with_entities(User.id, User.email, User.name, User.active, User.roles, User.password).filter_by(email=email, active=True).first()

    if user:

        is_logged = check_password_hash(user.password, password)

        if is_logged:
            
            status["success"] = True
            status["id"] = user.id
            status["email"] = user.email
            status["name"] = user.name
            status["active"] = user.active
            status["roles"] = user.roles
            status["message"] = "You have successfully logged in"
    

    return jsonify(status)


@login.route('/register', methods=['POST'])
def register():

    status = {
        "success": False,
        "id": 0,
        "email": None,
        "name": None,
        "active": False,
        "roles": None,
        "message": "E-mail or Password can not be blank!"
    }

    email = request.form['email']
    password = generate_password_hash(request.form["password"])
    name = request.form["name"]
    active = True
    roles = 1

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