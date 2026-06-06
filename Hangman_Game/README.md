# 🪢 Hangman

A classic terminal-based Hangman game built with Python. Guess the hidden word one letter at a time before the man is hanged!

---

## 🛠️ Description

The game picks a random word from a built-in list and gives you 10 attempts to guess it letter by letter. With each wrong guess, the hangman drawing gets closer to completion. Can you save him?

---

## ⚙️ Requirements

- Python 3.x
- No external libraries needed — uses only Python's built-in `random` module

---

## 🚀 How to Run

Clone the repository and run the game:

```bash
git clone https://github.com/anjalee-29/python-mini-projects/Hangman_Game.git
cd Hangman_Game
python hangman.py
```

---

## 🎮 How to Play

- Enter your name when prompted
- A random word will be chosen and displayed as underscores (e.g. `_ _ _ _ _`)
- Guess one letter at a time by typing it and pressing Enter
- You have **10 attempts** — each wrong guess costs one turn and draws more of the hangman
- Guess all letters correctly before running out of turns to win!

---

## 📁 Project Structure

```
├── hangman.py      # The game
└── README.md
```

---

## 📝 Notes

- Letters are case-insensitive — `A` and `a` are treated the same
- Re-guessing an already guessed letter won't cost you a turn
- The word is revealed if you lose so you know what it was


