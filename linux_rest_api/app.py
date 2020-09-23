from werkzeug.routing import BaseConverter
from flask import Flask
from . import system
from .filesystem import dirs_api, files_api


class FullPathConverter(BaseConverter):
    regex = ".*"


def create_app():
    app = Flask(__name__)

    # this is especially important for filesystem paths
    app.url_map.strict_slashes = False
    app.url_map.converters["fullpath"] = FullPathConverter

    app.register_blueprint(system.bp, url_prefix="/system")
    app.register_blueprint(dirs_api.bp, url_prefix="/dirs:")
    app.register_blueprint(files_api.bp, url_prefix="/files:")

    return app
