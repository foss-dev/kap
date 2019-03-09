from tracer.data.models import db, User, Role

class BaseConfig(object):
    ORIGINS = ["*"]
    SECRET_KEY = '\xb6]V~\x93\xcb\x1c\x12\xec\xcf\xa0&\x81b\xfc\x1a\xdc\x8b\xefAu\xa6\xd9\x9c'

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