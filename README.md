# 🧠 Typing Speed Test in Python

Welcome to the **Typing Speed Test** – **<u>a terminal-based Python application</u>** that helps users assess their typing speed and accuracy in a fun and interactive way!

---

## 📝 Project Description

This project randomly selects 10 sentences from a collection of 75 unique sentences. Users are then asked to type them as fast and accurately as possible within **60 seconds**. Once the timer is up, the program calculates the **number of words typed**, **correct words**, **words per minute (WPM)**, and **accuracy**.

---

## 🚀 Features

- ⏱️ 60-second countdown timer (runs in a separate thread)
- 🎯 Randomly selected non-repetitive sentences each round
- 🧮 Real-time measurement of:
  - Total words typed
  - Correct words
  - Accuracy (%)
  - Words Per Minute (WPM)
- 🔁 Option to retry multiple times

---

## 🛠️ Installation & Setup

1. **Clone this repository**  
   ```bash
   git clone https://github.com/Akrit22/checker.git
   cd checker

---
## 💡 Sample Output
```
Type the following 10 sentences exactly, and repeat as many times as you can in 1 minute.

1. The quick brown fox jumps over the lazy dog
2. A journey of a thousand miles begins with a single step
...
10. The violinist plays a haunting tune

Press Enter when you\'re ready to start...

**************Start typing now (1 minute):

[...User typing...]

************************** Results:
Words Typed:54
Correct Words:50
Words Per Minute (WPM): 50.00
Accuracy: 92.59%
```
---
## 👨‍💻 Technologies Used
- Python 3
- random module
- threading module
- time module
