from flask import Flask
from flask_cors import CORS

from tracer.api.admin.controllers import admin

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["*"]}})

app.register_blueprint(admin, url_prefix="/api/admin")

