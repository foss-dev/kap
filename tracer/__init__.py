from flask import Flask
from flask_cors import CORS

import config

from tracer.api.user.controllers import user
from tracer.api.login.controllers import login
from tracer.api.keys.controllers import keys
from tracer.data.models import db


app = Flask(__name__)

cors = CORS(app, resources={
    r"/api/*": {
        "origins": config.BaseConfig.ORIGINS
    }
})

config.configure_app(app)
db.init_app(app)


app.url_map.strict_slashes = False

app.register_blueprint(login, url_prefix="/api/login")
app.register_blueprint(user, url_prefix="/api/users")
app.register_blueprint(keys, url_prefix="/api/keys")

