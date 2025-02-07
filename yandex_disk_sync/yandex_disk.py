import requests
import os
from logger import logger
from config import YANDEX_DISK_TOKEN


class YandexDisk:
    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

    def __init__(self):
        self.headers = {"Authorization": f"OAuth {YANDEX_DISK_TOKEN}"}

    def create_folder(self, folder_path):
        """Создаёт папку на Яндекс.Диске, если её нет"""
        logger.info(f"Проверка существования папки: {folder_path}")
        url = f"{self.BASE_URL}?path={folder_path}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 404:
            logger.info(f"Папка {folder_path} не найдена, создаём...")
            response = requests.put(url, headers=self.headers)
            if response.status_code == 201:
                logger.info(f"Папка {folder_path} успешно создана")
            else:
                logger.error(f"Ошибка создания папки {folder_path}: {response.text}")

    def upload_file(self, local_path, remote_path):
        """Загружает файл на Яндекс.Диск"""
        folder_path = "/".join(remote_path.split("/")[:-1])  # Получаем путь к папке
        self.create_folder(folder_path)  # Создаём папку, если её нет

        logger.info(f"Загрузка файла: {local_path} → {remote_path}")
        url = f"{self.BASE_URL}/upload"
        params = {"path": remote_path, "overwrite": "true"}

        response = requests.get(url, headers=self.headers, params=params)

        if response.status_code == 200:
            upload_url = response.json()["href"]
            with open(local_path, "rb") as file:
                put_response = requests.put(upload_url, files={"file": file})
                if put_response.status_code == 201:
                    logger.info(f"Файл {local_path} успешно загружен на {remote_path}")
                else:
                    logger.error(f"Ошибка загрузки файла {local_path}: {put_response.text}")
        else:
            logger.error(f"Ошибка при получении ссылки на загрузку: {response.text}")

    def delete_file(self, remote_path):
        """Удаляет файл с Яндекс.Диска"""
        logger.info(f"Удаление файла: {remote_path}")
        url = f"{self.BASE_URL}?path={remote_path}"
        response = requests.delete(url, headers=self.headers)

        if response.status_code == 204:
            logger.info(f"Файл {remote_path} успешно удалён")
        else:
            logger.error(f"Ошибка при удалении файла {remote_path}: {response.text}")
