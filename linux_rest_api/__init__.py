from flask import Flask
from . import system
from .filesystem import dirs_api, files_api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(system.bp, url_prefix="/system")
    app.register_blueprint(dirs_api.bp, url_prefix="/dirs:")
    app.register_blueprint(files_api.bp, url_prefix="/files:")
    return app
