from flask import Flask

from workbench_app.blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    app = Flask(__name__, instance_relative_config=False)

    app.config.from_object('workbench_app.config.settings')
    # app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)

    return app
