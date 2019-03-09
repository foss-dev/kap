import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    roles = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, email, name, password, active, roles):
        self.email = email
        self.name = name
        self.password = password
        self.active = active
        self.roles = roles
    
    def __repr__(self):
        return '<User %r' % (self.email)

class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):

        self.name = name

    def __repr__(self):

        return '<Role %r>' % (self.name)


class Keys(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    application_id = db.Column(db.Integer())
    key = db.Column(db.Integer()) # uuid.NAMESPACE_DNS, (current timestamp + application id + user id + secret key)
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, user_id, application_id, key, active):

        self.user_id = user_id
        self.application_id = application_id
        self.key = key
        self.active = active