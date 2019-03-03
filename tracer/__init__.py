from flask import Flask
from flask_cors import CORS

import config

from tracer.api.user.controllers import user
from tracer.data.models import db


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["*"]}})

config.configure_app(app)
db.init_app(app)


app.register_blueprint(user, url_prefix="/api/users")

