# 🔥 AM-NOT-AFK

## 🚀 Overview

AM-NOT-AFK is a **powerful and customizable AFK prevention tool** that simulates
user activity to keep your system from going idle. It randomly moves the mouse
and simulates key presses at defined intervals, ensuring that your session
remains active.

---

## 🎯 Features

✅ **Fully Automated** – Runs in the background and prevents inactivity  
✅ **Customizable** – Set time intervals, movement ranges, and enable/disable
keystrokes  
✅ **Intelligent Keystroke Handling** – Uses special key mappings for accuracy  
✅ **Easy to Use** – Skip configuration prompts by pressing Enter to use default
values  
✅ **Colorful & Professional Logs** – Uses `rich` for enhanced logging and UI  
✅ **Graceful Exit** – Handles `CTRL+C` interruptions safely

---

## 🛠️ Installation

1. **Clone the repository**
   ```sh
   git clone https://github.com/your-username/am-not-afk.git
   cd am-not-afk
   ```
2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

---

## ⚡ Usage

Run the script using:

```sh
python afk_prevention.py
```

### 🔧 Configuration Options

The script will prompt you for configuration values:

- **Interval Between Actions (seconds)** _(default: 5 sec)_
- **Mouse Movement Range (pixels)** _(default: 20 px)_
- **Enable Keystrokes? (yes/no)** _(default: yes)_
- **Total Runtime (minutes, 0 for infinite)** _(default: 0, runs indefinitely)_

💡 **Tip:** Press **Enter** to skip a question and use the default value.

---

## 🛑 Stopping the Script

- Press **CTRL + C** to safely stop execution.
- The script will display a **shutdown message** before exiting.

---

## 🤝 Contributions

Want to improve this tool? Feel free to fork, modify, and submit a **pull
request**!

---

## 📜 License

This project is **open-source** and available under the **MIT License**.
