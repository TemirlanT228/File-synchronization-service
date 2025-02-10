import os
from dotenv import load_dotenv

load_dotenv()

YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")
LOCAL_FOLDER = os.getenv("LOCAL_FOLDER")
YANDEX_FOLDER = os.getenv("YANDEX_FOLDER")
SYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL", 60))
LOG_FILE = os.getenv("LOG_FILE")

# Проверяем, что все ключевые параметры заданы
if not YANDEX_TOKEN or not LOCAL_FOLDER or not YANDEX_FOLDER:
    raise ValueError("Ошибка конфигурации: Проверьте, что YANDEX_TOKEN, LOCAL_FOLDER и YANDEX_FOLDER заданы в .env")
