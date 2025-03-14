import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env (в файле должна быть переменная OPENAI_API_KEY)
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "gpt-4"
TEMPERATURE = 0.7
