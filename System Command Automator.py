import subprocess
import platform

def run_command(cmd):
    print(f"\n🛠️ Running: {cmd}")
    try:
        result = subprocess.run(
            cmd, 
            shell=True, 
            text=True, 
            capture_output=True,
            timeout=10
        )

        if result.returncode == 0:
            print("✅ Command executed successfully!")
            print("📥 Output:\n", result.stdout.strip())
        else:
            print("❌ Command failed with return code:", result.returncode)
            print("⚠️ Error:\n", result.stderr.strip())

    except subprocess.TimeoutExpired:
        print("⏳ Command timed out!")
    except Exception as e:
        print(f"🔥 Unexpected error: {e}")

def get_system_commands():
    system = platform.system()
    if system == "Windows":
        return [
            "systeminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\"",
            "wmic logicaldisk get size,freespace,caption",
            "powershell Get-Process | Sort-Object CPU -Descending | Select-Object -First 5"
        ]
    else:
        return [
            "uptime",
            "df -h",
            "free -m"
        ]

if __name__ == "__main__":
    commands = get_system_commands()
    for cmd in commands:
        run_command(cmd)
