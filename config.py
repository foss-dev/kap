from tracer.data.models import db, User, Role

class Development(object):
    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///kap.db'


config = {
    "development": "config.Development"
}

def configure_app(app):
    app.config.from_object(config['development'])