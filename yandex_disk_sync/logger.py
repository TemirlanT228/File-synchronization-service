from loguru import logger
import os
from config import LOG_FILE

# Удаляем старый лог, если он есть
if os.path.exists(LOG_FILE):
    os.remove(LOG_FILE)

# Настраиваем логгер
logger.add(LOG_FILE, format="{time} {level} {message}", level="INFO", rotation="1 MB", compression="zip")

logger.info("Логгер инициализирован")
