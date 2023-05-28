from flask import request
import requests
import json

API_KEY_GPT = "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"
API_ENDPOINT_GPT = "https://api.openai.com/v1/chat/completions"


def generate_chat_completion(messages):
    model = request.args.get('model', 'gpt-4')
    temperature = float(request.args.get('temperature', 1))
    max_tokens = request.args.get('max_tokens')

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY_GPT}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(
        API_ENDPOINT_GPT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        choices = response_data.get("choices")
        if choices and len(choices) > 0:
            message = choices[0].get("message")
            if message:
                content = message.get("content")
                if content:
                    return content
    raise Exception(f"Error {response.status_code}: {response.text}")
