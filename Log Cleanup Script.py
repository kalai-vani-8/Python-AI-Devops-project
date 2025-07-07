import os
import time
from datetime import datetime, timedelta

# === Configuration ===
LOG_DIR = "/var/log"  # Change this to any test folder to avoid deleting real system files
DAYS_OLD = 7  # Files older than this will be deleted

def clean_old_logs(log_dir, days_old):
    now = time.time()
    cutoff = now - (days_old * 86400)

    deleted_files = []

    for root, dirs, files in os.walk(log_dir):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path) and os.path.getmtime(file_path) < cutoff:
                try:
                    os.remove(file_path)
                    deleted_files.append(file_path)
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

    return deleted_files

if __name__ == "__main__":
    print("🔧 Running log cleanup...")
    deleted = clean_old_logs(LOG_DIR, DAYS_OLD)
    print(f"✅ Deleted {len(deleted)} files.")
