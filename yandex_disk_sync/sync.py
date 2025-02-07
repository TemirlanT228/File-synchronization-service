import time
from watchdog_handler import start_watching
from config import SYNC_INTERVAL
from logger import logger

if __name__ == "__main__":
    try:
        observer = start_watching()
        while True:
            time.sleep(SYNC_INTERVAL)
    except KeyboardInterrupt:
        logger.info("Синхронизация остановлена пользователем")
        observer.stop()
    observer.join()
