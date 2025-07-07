import os
from langchain.chat_models import ChatOpenAI

# Получение переменных окружения
BASE_URL = os.environ.get("LLM_BASE_URL")
API_KEY = os.environ.get("LLM_API_KEY")
MODEL_NAME = os.environ.get("LLM_MODEL", "meta-llama/Llama-3.3-70B-Instruct")

if not BASE_URL or not API_KEY:
    raise ValueError("Переменные окружения LLM_BASE_URL и LLM_API_KEY должны быть заданы.")

# Инициализация клиента
client = ChatOpenAI(
    base_url=BASE_URL,
    api_key=API_KEY,
    model=MODEL_NAME
)
