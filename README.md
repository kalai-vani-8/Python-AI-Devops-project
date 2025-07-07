# Python-AI-Devops-project

# 🔧 Python DevOps Automation – Day 1 of My GenAI Journey

Hi! I’m Nilla 👋 — a DevOps engineer learning Generative AI by building real-world automation tools. This project is from **Day 1** of my learning series, where I focused on using **Python** to automate key DevOps tasks.

---

## 📌 Project Overview

This repo contains simple yet powerful Python scripts to:
- 🧹 Clean up old log files
- 💽 Monitor disk usage
- ⚙️ Automate system commands (uptime, memory, etc.)

These are foundational DevOps tasks, and we’ll soon plug in **LLMs** to make them smarter — like summarizing log errors or generating alerts using GenAI.

---

## 🛠️ Features

### `log_cleanup.py`
- Deletes log files older than X days from a specified directory
- Logs deleted files to the console

### `disk_monitor.py`
- Displays total, used, and free disk space
- Alerts if usage > 80%

### `system_check.py`
- Runs system commands based on your OS (Windows/Linux)
- Shows command output and success/failure status

---

## 💡 Skills Practiced

- ✅ Python scripting
- ✅ Automation using `os`, `shutil`, and `subprocess`
- ✅ OS detection and CLI integration
- 🔜 Integrating GenAI (LLMs, prompt-based log analysis)

---

## 🧰 Tech Stack

- Python 3.11
- Linux CLI / Windows PowerShell
- GitHub
- VSCode

---

## 📦 How to Run

```bash
# Clone this repository
git clone https://github.com/yourusername/genai-python-devops-day1.git
cd genai-python-devops-day1

# Run individual scripts
python log_cleanup.py
python disk_monitor.py
python system_check.py
