import time
import os
import sys
import logging
from watchdog.observers import Observer
from watchdog_handler import SyncHandler
from dotenv import load_dotenv
from logger import logger

load_dotenv()
LOCAL_FOLDER = os.getenv("LOCAL_FOLDER")
SYNC_INTERVAL = int(os.getenv("SYNC_INTERVAL", 60))

if not os.path.exists(LOCAL_FOLDER):
    logger.error("Локальная папка %s не найдена.", LOCAL_FOLDER)
    sys.exit(1)


def start_sync():
    logger.info("Начата синхронизация: %s -> Yandex.Disk", LOCAL_FOLDER)
    observer = Observer()
    event_handler = SyncHandler()
    observer.schedule(event_handler, LOCAL_FOLDER, recursive=True)
    observer.start()
    logger.info("Запущен файловый наблюдатель для %s", LOCAL_FOLDER)

    try:
        while True:
            time.sleep(SYNC_INTERVAL)
    except KeyboardInterrupt:
        logger.info("Синхронизация остановлена пользователем.")
        observer.stop()
    observer.join()


if __name__ == "__main__":
    start_sync()
