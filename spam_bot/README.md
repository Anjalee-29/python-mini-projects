# 🤖 Spam Bot

A fun Python spam bot to prank your friends — sends repeated messages automatically by simulating keyboard input. Two bots included!

> ⚠️ **For educational/prank purposes only. Use responsibly and only with consent.**

---

## 🛠️ Description

- **bot1.py** — You type a message, it spams it repeatedly until you press `q` to stop
- **bot2.py** — Reads words from `text.txt` and spams them one by one automatically

---

## ⚙️ Requirements

- Python 3.x
- Windows or Linux (macOS may have permission issues with `pyautogui`)

Install dependencies:

```bash
pip install -r requirements.txt
```

> **Linux users** may need to install an additional dependency for `keyboard`:
> ```bash
> sudo pip install keyboard
> ```
> or run the script with `sudo`:
> ```bash
> sudo python3 bot1.py
> ```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/Anjalee-29/python-mini-projects/spam_bot.git
cd spam_bot
pip install -r requirements.txt
```

### Run bot1 (custom message spammer):

```bash
python bot1.py       # Windows
python3 bot1.py      # Linux
```

- Enter your message when prompted
- Switch to the target window (chat, notepad, etc.)
- The bot starts after a 3-second countdown
- Press **`q`** to stop

### Run bot2 (text file spammer):

```bash
python bot2.py       # Windows
python3 bot2.py      # Linux
```

- Words from `text.txt` are sent one by one automatically
- Press **`q`** to stop between words

---

## 📁 Project Structure

```
├── bot1.py          # Custom message spam bot
├── bot2.py          # Text file word spam bot
├── text.txt         # Words to spam (used by bot2)
├── requirements.txt # Dependencies
└── README.md
```

---

## 📝 Notes

- `pyautogui.typewrite()` only supports plain ASCII characters — special characters or emojis may not be typed correctly
- Make sure to click into the target window **before** the countdown ends
- The `.pyc` compiled cache file does not need to be committed — it's listed in `.gitignore`

