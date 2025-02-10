# File Synchronization Service

## Overview
This project is a file synchronization service that monitors a local folder and synchronizes its contents with Yandex.Disk cloud storage. It automatically uploads new and modified files to Yandex.Disk and deletes files from the cloud when they are removed locally. The service is designed to protect user data, ensure backup availability, and demonstrate practical skills in working with HTTP requests, file operations, error handling, and logging.

## Features
- **Automatic Monitoring:** Uses the `watchdog` library to monitor changes (creation, modification, deletion) in a specified local folder.
- **Cloud Synchronization:** Automatically uploads, updates, and deletes files on Yandex.Disk using the Yandex.Disk API.
- **Logging:** All synchronization operations and errors are logged using Python's built-in `logging` module (with output both to the console and a log file).
- **Configuration:** All parameters (local folder path, Yandex.Disk folder name, API token, sync interval, and log file path) are configured via a `.env` file using `python-dotenv`.
- **Error Handling:** The service gracefully handles errors (e.g., network issues or file access errors) without interrupting the synchronization process.

## Requirements
- Python 3.x
- Required Python packages (listed in `requirements.txt`):
  - `requests`
  - `watchdog`
  - `python-dotenv`

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/file-synchronization-service.git
cd file-synchronization-service
```
###2. 

Create a Virtual Environment and Activate It
```bash
python3 -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows
```


###3.
 Install Dependencies
 ```bash
 pip install -r requirements.txt
```




###4.
Configure Environment Variables
Create a .env file in the project root with the following content (replace placeholder values with your actual settings):
```bash
YANDEX_TOKEN=your_yandex_disk_token
LOCAL_FOLDER=/path/to/your/local/folder
YANDEX_FOLDER=MySyncFolder
SYNC_INTERVAL=60
LOG_FILE=sync.log
```
###5.Usage
Start the Service
```bash
python sync.py
```
