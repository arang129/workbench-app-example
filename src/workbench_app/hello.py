import os
from flask import Flask, Blueprint

# Prefix configuration
root_url_prefix = os.getenv('FLASK_APP_URL_PREFIX', '/')

# Create app
app = Flask(__name__)
root_bp = Blueprint("root", __name__, template_folder='templates')


@root_bp.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


app.register_blueprint(root_bp, url_prefix=root_url_prefix)
