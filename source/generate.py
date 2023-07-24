from mysql.connector import connect

from . import configs
from .openai_call import chat_completion_call

def generate_sql(query, tables_desc: list[dict]):
    """Generates SQL command based on user query and tables given"""

    prompt = ""
    for table in tables_desc:
        prompt += f"Table name: {table['name']}\n\nTable schema:\n"
        for attribute in table["desc"]:
            prompt += f"{attribute}\n"
        prompt += '\n'
        if table["samples"]:
            prompt += f"Sample rows:\n"
            for sample in table["samples"]:
                prompt += f"{sample}\n"
            prompt += '\n'
    prompt += f"Question: {query}"
    return chat_completion_call(
        prompt=prompt,
        model=configs.MODEL,
        sys_msg=configs.SYSTEM_MESSAGE,
        prev_msgs=configs.PREVIOUS_MESSAGES
    )

def generate_table_desc(table_list, user, key, host, db):
    """Gets the descriptions and sample rows of the tables given from database"""

    connection = connect(
        user=user,
        password=key,
        host=host,
        db=db
    )
    cur = connection.cursor()

    tables_desc = []
    for table in table_list:
        table_dict = {}
        table_dict["name"] = table
        cur.execute(f"DESC {table}")
        table_dict["desc"] = cur.fetchall()
        cur.execute(f"SELECT * from {table} LIMIT 3")
        table_dict["samples"] = cur.fetchall()
        tables_desc.append(table_dict)    

    cur.close()
    connection.close()
    return tables_desc
