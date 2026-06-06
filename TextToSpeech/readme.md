# 🔊 Text To Speech

A simple desktop app built with Python that converts typed text into speech using a clean GUI.

---

## 🛠️ Description

Type anything into the input box, click the button, and the app will read it out loud. Built with `tkinter` for the GUI and `pyttsx3` for text-to-speech — works completely offline, no API needed.

---

## ⚙️ Requirements

- Python 3.x
- `pyttsx3` — for text-to-speech
- `tkinter` — for the GUI (built into Python on Windows/macOS

**Linux users** need to install `tkinter` separately:
```bash
sudo apt-get install python3-tk
```

---

## 🚀 Installation & Running

1. Clone the repository:
```bash
git clone https://github.com/anjalee-29/python-mini-projects/TextToSpeech.git
cd TextToSpeech
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
python Text_To_Speech.py
```

---

## 🎮 How to Use

- Type any text into the input box
- Click **CLICK ME!**
- The app will read your text out loud

---

## 📁 Project Structure

```
├── Text_To_Speech.py   # Main application
├── requirements.txt    # Dependencies
└── README.md
```

---

## 📝 Notes

- Works on Windows, macOS, and Linux
- Runs fully offline — no internet connection required
- On Linux, the voice engine uses `espeak` by default. Install it if you have no audio output:
  ```bash
  sudo apt-get install espeak
  ```
