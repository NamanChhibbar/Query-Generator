import os, openai
from dotenv import load_dotenv
from mysql.connector import connect
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from source import configs
from source.generate import generate_sql

@csrf_exempt
def respond(request):

    load_dotenv(configs.PATH_TO_ENV)
    body = loads(request.body)

    openai.api_key = os.getenv("OPENAI_KEY")
    db_user = os.getenv("MYSQL_USER")
    db_key = os.getenv("MYSQL_KEY")
    db_host = os.getenv("MYSQL_HOST")
    db = os.getenv("MYSQL_DB")

    user_query = body["user_query"]
    table_list = body["tables"]

    connection = connect(
        user=db_user,
        password=db_key,
        host=db_host,
        db=db
    )
    cur = connection.cursor()

    tables = []
    for table in table_list:
        table_dict = {}
        table_dict["name"] = table
        cur.execute(f"DESC {table}")
        table_dict["desc"] = cur.fetchall()
        cur.execute(f"SELECT * from {table} LIMIT 3")
        table_dict["samples"] = cur.fetchall()
        tables.append(table_dict)

    message, usage = generate_sql(user_query, tables)

    cur.close()
    connection.close()
    return JsonResponse({
        "success": True,
        "message": message,
        "usage": usage
    })
