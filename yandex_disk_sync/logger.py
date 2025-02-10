import logging
from config import LOG_FILE, LOCAL_FOLDER

# Создаем логгер
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler: пишет в файл
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)

# Console handler: выводит в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Форматтер для обоих хендлеров
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Добавляем обработчики в логгер
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Логгер инициализирован. Локальная папка: %s", LOCAL_FOLDER)
