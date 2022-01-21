# Django_server

Django_server is the server used to store the coordinates sent from [Unity_client](https://github.com/Elchma/unity_client) projet

## Installation

### Create and activate a virtual env

```bash
python -m venv env
. env/Scripts/activate # or . env/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Apply migrations to the database

```bash
cd app
python manage.py migrate
```

### (Optional) Create a superuser
```bash
python manage.py createsuperuser
```

## Usage

### Start server
```
python manage.py runserver
```

### Coordinates

The coordinate's endpoint is `http://127.0.0.1:8000/coordinate/`

#### Post

You can send coordinates using a form-data containing the data `x`, `y` and `z`

#### Options

Each field are described in the `OPTIONS` method where you can know if it's required, min value, max value...