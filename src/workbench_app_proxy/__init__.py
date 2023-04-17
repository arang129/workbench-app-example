import logging
from pathlib import Path
from workbench_app_proxy.jupyter_config import config


def _get_env(port, base_url):
    """
    Returns a dict containing environment settings to launch the Web App.

    Args:
        port (int): Port number on which the Web app will be started. Ex: 8888
        base_url (str): Controls the prefix in the url on which
                        the Web App will be available.
                        Ex: localhost:8888/base_url/index.html

    Returns:
        [Dict]: Containing environment settings to launch the Web application.
    """

    return {
        "FLASK_RUN_PORT": str(port),
        "APP_BASE_URL": f"{base_url}webapp",
        "FLASK_APP": config['flask_app'],
    }


def setup_app():
    """
    Setup application.

    This method is run by jupyter-server-proxy package to launch the Web app.
    """

    logging.basicConfig(level="INFO")
    logger = logging.getLogger("WorkbenchAppProxy")
    logger.setLevel("INFO")
    logger.info("Initializing Jupyter Workbench Proxy")

    icon_path = Path(__file__).parent / "app-icon.svg"
    executable_name = "flask"
    host = "127.0.0.1"
    logger.debug(f"Icon_path:  {icon_path}")
    logger.debug(f"Launch Command: {executable_name}")
    logger.debug(f"Extension Name: {config['extension_name']}")
    return {
        "command": [
            executable_name,
            "run",
            "--host={host}".format(host=host),
        ],
        "timeout": 100,
        "environment": _get_env,
        "absolute_url": True,
        "launcher_entry": {"title": "Open App", "icon_path": icon_path},
    }
