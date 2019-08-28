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
    key = db.Column(db.String(60)) # uuid.NAMESPACE_DNS, (current timestamp + application id + user id + secret key)
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, user_id, application_id, key, active):

        self.user_id = user_id
        self.application_id = application_id
        self.key = key
        self.active = active
    
    def __repr__(self):

        return '<Key %r>' % self.key


class Applications(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    repo = db.Column(db.String(255))
    active = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, user_id, title, description, repo, active):

        self.user_id = user_id
        self.title = title
        self.description = description
        self.repo = repo
        self.active = active
    
    def __repr__(self):

        return '<Application %r>' % self.title

class Languages(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    logo_path = db.Column(db.String(150))

    def __init__(self, name, logo_path):

        self.name = name
        self.logo_path = logo_path
    
    def __repr__(self):

        return '<Language %r>' % self.name

class ExceptionTypes(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.Text())
    url = db.Column(db.String(255))

    def __init__(self, name, description, url):

        self.name = name
        self.description = description
        self.url = url
    
    def __repr__(self):

        return '<Exception Type %r>' % self.name

class Logs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer())
    application_id = db.Column(db.Integer())
    language_id = db.Column(db.Integer())
    exception_type_id = db.Column(db.Integer())
    line_number = db.Column(db.Integer())
    column_number = db.Column(db.Integer())
    code = db.Column(db.Integer())
    file_name = db.Column(db.String(150))
    method_name = db.Column(db.String(150))
    message = db.Column(db.Text())
    trace = db.Column(db.String(255))
    query = db.Column(db.Text())
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, **kwargs):

        super(Logs, self).__init__(**kwargs)
    
    def __repr__(self):

        return '<Log %r>' % self.message
