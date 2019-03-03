from tracer.data.models import db, User, Role

class BaseConfig(object):
    ORIGINS = ["*"]

class Development(BaseConfig):
    PORT = 5000
    DEBUG = True
    TESTING = False
    ENV = 'dev'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///kap.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    "development": "config.Development"
}

def configure_app(app):
    app.config.from_object(config['development'])