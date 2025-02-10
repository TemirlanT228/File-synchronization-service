import requests
import os
from logger import logger
from config import YANDEX_TOKEN, YANDEX_FOLDER

class YandexDisk:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"OAuth {self.token}"}
        self.base_url = "https://cloud-api.yandex.net/v1/disk"

    def _create_folder_if_not_exists(self, folder_path):
        """Проверяет наличие удалённой папки и создаёт её, если её нет."""
        url = f"{self.base_url}/resources"
        params = {"path": folder_path}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 404:
            logger.info("Папка %s не найдена, создаём...", folder_path)
            response = requests.put(url, headers=self.headers, params=params)
            if response.status_code == 201:
                logger.info("Папка %s создана.", folder_path)
            else:
                logger.error("Ошибка создания папки %s: %s", folder_path, response.text)
        elif response.status_code == 200:
            logger.info("Папка %s существует.", folder_path)
        else:
            logger.error("Ошибка проверки папки %s: %s", folder_path, response.text)

    def upload(self, local_path, yandex_path):
        """Загружает (или обновляет) файл на Яндекс.Диске."""
        folder_path = "/".join(yandex_path.split("/")[:-1])
        self._create_folder_if_not_exists(folder_path)

        logger.info("Загрузка файла: %s -> %s", local_path, yandex_path)
        url = f"{self.base_url}/resources/upload"
        params = {"path": yandex_path, "overwrite": "true"}
        response = requests.get(url, headers=self.headers, params=params)
        if response.status_code == 200:
            upload_url = response.json().get("href")
            try:
                with open(local_path, "rb") as f:
                    put_response = requests.put(upload_url, files={"file": f})
                if put_response.status_code in (200, 201, 202):
                    logger.info("Файл %s успешно загружен в %s", local_path, yandex_path)
                else:
                    logger.error("Ошибка загрузки файла %s: %s", local_path, put_response.text)
            except Exception as e:
                logger.error("Исключение при загрузке файла %s: %s", local_path, str(e))
        else:
            logger.error("Ошибка получения URL для загрузки файла %s: %s", local_path, response.text)

    def delete(self, yandex_path):
        """Удаляет файл с Яндекс.Диска."""
        logger.info("Удаление файла с Яндекс.Диска: %s", yandex_path)
        url = f"{self.base_url}/resources"
        params = {"path": yandex_path, "permanently": "true"}
        response = requests.delete(url, headers=self.headers, params=params)
        if response.status_code in (200, 204):
            logger.info("Файл %s удалён с Яндекс.Диска", yandex_path)
        elif response.status_code == 404:
            logger.warning("Файл %s не найден на Яндекс.Диске", yandex_path)
        else:
            logger.error("Ошибка удаления файла %s: %s", yandex_path, response.text)

    def exists(self, yandex_path):
        """Проверяет, существует ли файл на Яндекс.Диске."""
        url = f"{self.base_url}/resources"
        params = {"path": yandex_path}
        response = requests.get(url, headers=self.headers, params=params)
        return response.status_code == 200
