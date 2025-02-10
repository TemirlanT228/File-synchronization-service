# File-synchronization-service
## 📌 **Project Description**  
This project is a file synchronization service between a **local folder** and **Yandex.Disk** cloud storage.  

### **Main Features**  
- **Automatic tracking** of changes in the specified local folder.  
- **Uploading new and modified files** to Yandex.Disk.  
- **Deleting files from the cloud** if they are removed locally.  
- **Logging operations** using `loguru`.  

---

## ⚙️ **Installation and Setup**  

### 1️⃣ **Clone the Repository**  
git clone https://github.com/your-repo/yandex_disk_sync.git
cd yandex_disk_sync

2️⃣ Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Configure Environment Variables

Create a .env file in the project root and add the following:

YANDEX_DISK_TOKEN=your_yandex_disk_token

LOCAL_FOLDER=/Users/temirlan/File-synchronization-service/yandex_disk_sync

REMOTE_FOLDER=MySyncFolder

SYNC_INTERVAL=10

LOG_PATH=sync.log

Variable Descriptions:

YANDEX_DISK_TOKEN – OAuth token for Yandex.Disk API access.

LOCAL_FOLDER – Path to the local folder for synchronization.

REMOTE_FOLDER – Folder in Yandex.Disk where files will be uploaded.

SYNC_INTERVAL – Synchronization interval (in seconds).

LOG_PATH – Log file path.

🚀 Run the Service
python sync.py

Once started:

The program checks if the MySyncFolder exists in Yandex.Disk (creates it if not).
It starts monitoring changes in the local folder.
Automatically uploads new/modified files and deletes missing ones.

🔧 Project Structure
yandex_disk_sync/

│── .env                      # Configuration file (API token, folders, etc.)

│── sync.py                   # Main script to run synchronization

│── yandex_disk.py            # Class for interacting with Yandex.Disk API

│── watchdog_handler.py        # File change monitoring

│── requirements.txt           # Project dependencies

│── venv/                      # Virtual environment (ignored in Git)

│── sync.log                   # Log file


📜 Files and Their Purpose

1️⃣ sync.py (Main Script)

This file launches the synchronization service. It initializes:

Logger (loguru)

YandexDisk class (handles API requests)

WatchdogHandler class (monitors local folder changes)

2️⃣ yandex_disk.py (YandexDisk API Class)

Handles all interactions with the Yandex.Disk API, including:

Checking and creating folders

Uploading and deleting files

Fetching file and folder metadata

3️⃣ watchdog_handler.py (Folder Monitoring)

Uses the watchdog library to detect file changes and trigger synchronization.




