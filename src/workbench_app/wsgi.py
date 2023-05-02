from workbench_app.app import create_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response
import os

root_url_prefix = os.getenv('FLASK_APP_URL_PREFIX', '/')

app = create_app()

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,
    {
        root_url_prefix: app,
    }
)
