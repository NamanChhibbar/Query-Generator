# Query Generation
A simple server setup to receive requests with a user query and list of tables and respond with message and usage.

## Server setup

### Install python dependencies
Create a python virtual environment and run
```
pip install -r requirements.txt
```
to install the python dependencies

### Create `keys.env`
Create `keys.env` using the format specified in `.env-example` and set the path of `keys.env` in `source/configs.py`.

## Server startup
Run
```
python manage.py runserver
```
to start the server.
