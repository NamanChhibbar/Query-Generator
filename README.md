# Query Generation
A simple server setup to generate SQL queries using OpenAI's chat completion.

## Server Setup

### Install Python Dependencies
Create a Python virtual environment and run
```
pip install -r requirements.txt
```
to install the Python dependencies

### Create `credentials.env`
Create `.env` file using the format specified in `.env.example` and set the path of `.env` in `source/configs.py`.

## Server startup
Run
```
python manage.py runserver
```
to start the server.

## API request format
The request body must be in JSON format, containing 2 keys - "userQuery" and "table_list". The data type of "userQuery" is a string, and "table_list" is a list.

## API response format
The json response will contain 3 keys - "success", "message", and "usage". "success" will have a boolean value corresponding to whether the request was successful or not. "message" will contain a string which will be the response. "usage" will contain an integer corresponding to number of tokens used in the query generation.
