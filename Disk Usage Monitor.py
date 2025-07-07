import shutil

def check_disk_usage(path="/"):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100

    print(f"📦 Disk Usage for {path}:")
    print(f"  Total: {total // (2**30)} GB")
    print(f"  Used: {used // (2**30)} GB")
    print(f"  Free: {free // (2**30)} GB")
    print(f"  Usage: {percent_used:.2f}%")

    if percent_used > 80:
        print("🚨 Warning: High disk usage!")
    else:
        print("✅ Disk usage is within limits.")

if __name__ == "__main__":
    check_disk_usage("/")
