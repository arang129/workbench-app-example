# workbench-app-example

Create virtual environment if not existing yet:

```
python3 -m pip install virtualenv
python3 -m venv env
```

Activate virtual environment:

```
source env/bin/activate
```

Install dependencies:

```
python3 -m pip install -r requirements.txt
```

Start your web application and keep it running:

```
flask --app src/workbench_app/hello run
```

Open in browser: http://127.0.0.1:5000/

## Web application

```
src/workbench_app
```

## Jupyter proxy

```
src/workbench_app_proxy
```

## Jupyterlab extension

```
src/workbench_app_labextension
```

