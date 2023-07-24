import os, openai
from dotenv import load_dotenv
from json import loads
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from source import configs
from source.generate import generate_sql, generate_table_desc

@csrf_exempt
def respond(request):

    load_dotenv(configs.PATH_TO_ENV)
    body = loads(request.body)
    openai.api_key = os.getenv("OPENAI_KEY")

    tables = generate_table_desc(
        table_list=body["table_list"],
        user=os.getenv("MYSQL_USER"),
        key=os.getenv("MYSQL_KEY"),
        host=os.getenv("MYSQL_HOST"),
        db=os.getenv("MYSQL_DB")
    )

    message, usage = generate_sql(
        query=body["userQuery"],
        tables_desc=tables
    )

    return JsonResponse({
        "success": True,
        "message": message,
        "usage": usage
    })
