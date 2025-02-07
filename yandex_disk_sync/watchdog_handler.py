import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from yandex_disk import YandexDisk
from config import LOCAL_FOLDER, YANDEX_DISK_FOLDER
from logger import logger


class SyncHandler(FileSystemEventHandler):
    """Обработчик событий файловой системы"""

    def __init__(self, yandex_disk):
        self.yandex_disk = yandex_disk

    def on_created(self, event):
        if event.is_directory:
            return
        local_path = event.src_path
        remote_path = f"{YANDEX_DISK_FOLDER}/{os.path.basename(local_path)}"
        self.yandex_disk.upload_file(local_path, remote_path)

    def on_deleted(self, event):
        if event.is_directory:
            return
        remote_path = f"{YANDEX_DISK_FOLDER}/{os.path.basename(event.src_path)}"
        self.yandex_disk.delete_file(remote_path)


def start_watching():
    """Запускает наблюдатель за папкой"""
    logger.info(f"Запуск отслеживания папки: {LOCAL_FOLDER}")
    yandex_disk = YandexDisk()
    event_handler = SyncHandler(yandex_disk)
    observer = Observer()
    observer.schedule(event_handler, LOCAL_FOLDER, recursive=False)
    observer.start()
    return observer
