from flask import Flask
import os

from workbench_app.blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('workbench_app.config.settings')
    # app.config.from_pyfile('settings.py', silent=True)

    # root_url_prefix = os.getenv('FLASK_APP_URL_PREFIX', '/')

    # app.register_blueprint(page, url_prefix=root_url_prefix)
    if settings_override:
        app.config.update(settings_override)

    app.register_blueprint(page)

    return app
