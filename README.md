# workbench-app-example

## Jupyter proxy

[Jupyter-example-proxy](https://github.com/huntdatacenter/jupyter-example-proxy) is using this package as an example of web application that can be started from Workbench.

## Web application example

Just a random web applications that says hello world (you should replace this with your own):

```
src/workbench_app
```

## Development

Create virtual environment if not existing yet:

```
python3 -m pip install virtualenv
python3 -m venv env
```

Activate virtual environment:

```bash
source env/bin/activate
```

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Start your web application and keep it running:

```bash
flask --app src/workbench_app/wsgi run
```

Open in browser: http://127.0.0.1:5000/

### Running with gunicorn

```bash
gunicorn -w 4 workbench_app.wsgi:app --bind=127.0.0.1:5000
```

### Install from repo

Direct setup for development / testing purposes:

```bash
python3 -m pip install git+https://github.com/huntdatacenter/workbench-app-example.git@main#egg=workbench-app-example
```
