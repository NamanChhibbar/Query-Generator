from . import configs
from .openai_call import chat_completion_call

def generate_sql(query, tables: list[dict]):
    prompt = ""
    for table in tables:
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
