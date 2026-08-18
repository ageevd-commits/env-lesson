import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY не найден. Проверь файл .env")

print(".env работает!")
print("Ключ найден:", api_key[:7] + "..." + api_key[-4:])