from consts import SYSTEM_PROMPT, MODEL_NAME, MODEL_URL, MAX_NEW_TOKENS, TEMPERATURE, OPENAI_TOKEN
import requests

from script_utils import get_logger

LOGGER = get_logger()


def get_messages(
        question: str,
        context: str,
        system_prompt: str = SYSTEM_PROMPT
) -> list[dict[str, str]]:
    history = []
    if context and system_prompt:
        system_message = {
            "role": "system",
            "content": system_prompt + '\n' + context
        }
        history.append(system_message)
    if question:
        user_message = {
            "role": "user",
            "content": question
        }
        history.append(user_message)
    LOGGER.debug(f"Got history: {history}")
    return history


def call_model(
        messages: list[dict[str, str]],
        model_name: str = MODEL_NAME,
        url_out: str = MODEL_URL,
        max_new_tokens: int = MAX_NEW_TOKENS,
        temperature: float = TEMPERATURE
) -> str:
    data = {
        'model': model_name,
        'messages': messages,
        'max_tokens': max_new_tokens,
        'temperature': temperature
    }
    headers = {
        "Authorization": f"Bearer {OPENAI_TOKEN}"
    }
    response = requests.post(
        url_out,
        json=data,
        headers=headers,
        timeout=1000
    )
    answer = response.json()['choices'][0]['message']['content']
    LOGGER.debug(f"Got answer: {answer}")
    return answer
