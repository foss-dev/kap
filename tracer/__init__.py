from flask import Flask
from flask_cors import CORS

from tracer.api.user.controllers import user

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["*"]}})

app.register_blueprint(user, url_prefix="/api/user")

