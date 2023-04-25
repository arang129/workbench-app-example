from workbench_app.app import create_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
import os

root_url_prefix = os.getenv('FLASK_APP_URL_PREFIX', '/')

app = DispatcherMiddleware(
    Response('Not Found', status=404),
    {
        root_url_prefix: create_app(),
    }
)