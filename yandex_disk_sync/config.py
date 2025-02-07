import os
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

# Читаем конфигурацию
YANDEX_DISK_TOKEN = os.getenv("YANDEX_DISK_TOKEN")
LOCAL_FOLDER = os.getenv("LOCAL_FOLDER")
YANDEX_DISK_FOLDER = os.getenv("YANDEX_DISK_FOLDER")
LOG_FILE = os.getenv("LOG_FILE")
SYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL", 60))  # Значение по умолчанию 60 сек.

# Проверяем, что все переменные заданы
required_vars = ["YANDEX_DISK_TOKEN", "LOCAL_FOLDER", "YANDEX_DISK_FOLDER", "LOG_FILE"]
for var in required_vars:
    if not globals()[var]:
        raise ValueError(f"Переменная {var} не задана в файле .env")
