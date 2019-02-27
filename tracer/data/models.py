from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())

    def __init__(self, email, password, active):
        self.email = email
        self.password = password
        self.active = active
    
    def __repr__(self):
        return '<User %r' % (self.email)