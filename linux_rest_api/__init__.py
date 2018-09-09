from flask import Flask
from . import system


def create_app():
    app = Flask(__name__)
    app.register_blueprint(system.bp, url_prefix="/system")
    return app
