import os
from watchdog.events import FileSystemEventHandler
from yandex_disk import YandexDisk
from dotenv import load_dotenv
from logger import logger

load_dotenv()
LOCAL_FOLDER = os.getenv("LOCAL_FOLDER")
YANDEX_FOLDER = os.getenv("YANDEX_FOLDER")
YANDEX_TOKEN = os.getenv("YANDEX_TOKEN")

# Создаем объект для работы с Яндекс.Диском
yandex = YandexDisk(YANDEX_TOKEN)

IGNORE_EXTENSIONS = {".pyc"}
IGNORE_FOLDERS = {"__pycache__"}

def should_ignore(file_path):
    filename = os.path.basename(file_path)
    if any(filename.endswith(ext) for ext in IGNORE_EXTENSIONS):
        return True
    if any(ign in file_path for ign in IGNORE_FOLDERS):
        return True
    return False

class SyncHandler(FileSystemEventHandler):
    """Обработчик событий для синхронизации локальной папки с Яндекс.Диском."""

    def on_created(self, event):
        if event.is_directory or should_ignore(event.src_path):
            return
        logger.info("[WATCHDOG] Файл создан: %s", event.src_path)
        local_path = event.src_path
        remote_path = local_path.replace(LOCAL_FOLDER, YANDEX_FOLDER)
        try:
            yandex.upload(local_path, remote_path)
            logger.info("Файл загружен: %s", remote_path)
        except Exception as e:
            logger.error("Ошибка загрузки %s: %s", local_path, e)

    def on_deleted(self, event):
        if event.is_directory or should_ignore(event.src_path):
            return
        logger.info("[WATCHDOG] Файл удалён: %s", event.src_path)
        remote_path = event.src_path.replace(LOCAL_FOLDER, YANDEX_FOLDER)
        try:
            if yandex.exists(remote_path):
                yandex.delete(remote_path)
                logger.info("Файл удалён из облака: %s", remote_path)
            else:
                logger.warning("Файл %s отсутствует в облаке", remote_path)
        except Exception as e:
            logger.error("Ошибка удаления %s: %s", remote_path, e)

    def on_modified(self, event):
        if event.is_directory or should_ignore(event.src_path):
            return
        logger.info("[WATCHDOG] Файл изменён: %s", event.src_path)
        local_path = event.src_path
        remote_path = local_path.replace(LOCAL_FOLDER, YANDEX_FOLDER)
        try:
            yandex.upload(local_path, remote_path)
            logger.info("Файл обновлён: %s", remote_path)
        except Exception as e:
            logger.error("Ошибка обновления %s: %s", local_path, e)
