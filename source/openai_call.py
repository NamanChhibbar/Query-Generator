import openai

def chat_completion_call(prompt, model, sys_msg: str="", prev_msgs=[]):

    messages = [{"role": "system", "content": sys_msg}] if sys_msg else []
    messages.extend(prev_msgs)
    messages.append({
        "role": "user",
        "content": prompt
    })
    try:
        response = openai.ChatCompletion.create(model=model, messages=messages)
    except:
        return None, 0
    
    message = None
    usage = 0
    if response["choices"][0]["finish_reason"] == "stop":
        message = response["choices"][0]["message"]["content"]
        usage = response["usage"]["total_tokens"]
    return message, usage
