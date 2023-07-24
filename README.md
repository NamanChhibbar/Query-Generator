# Query Generation
A simple server setup to generate SQL queries using OpenAI's chat completion.

## Server setup

### Install python dependencies
Create a python virtual environment and run
```
pip install -r requirements.txt
```
to install the python dependencies

### Create `credentials.env`
Create `credentials.env` using the format specified in `.env-example` and set the path of `credentials.env` in `source/configs.py`.

## Server startup
Run
```
python manage.py runserver
```
to start the server.

## API request format
The request body must be of json format containing 2 keys - "userQuery" and "table_list". Data type of "userQuery" is a string and "table_list" is a list.

## API response format
The json response will contain 3 keys - "success", "message", and "usage". "success" will have a boolean value corresponding to whether the request was successful or not. "message" will contain a string which will be the response. "usage" will contain an integer corresponding to number of tokens used in the query generation.
