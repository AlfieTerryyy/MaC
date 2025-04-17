# 🎙️ MAC — Mimic and Communicate

MAC is a speech-driven assistant built with Flask that listens to your voice, understands patterns, and responds with spoken replies using eSpeak. It runs entirely on your Linux machine.

## 🧠 Features

- 🎤 Voice input via web browser
- 🗣️ Text-to-speech responses using `eSpeak`
- 🧩 Pattern matching for conversational replies
- 🗃️ Conversation logging with SQLite
- 🌐 Web interface using Flask
- 🐍 Fully isolated with Python `venv`

---

## 🚀 Quick Start (Linux)

### 1. Clone the repository

```bash
git clone https://github.com/AlfieTerryyy/MaC
cd MaC
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install Flask SpeechRecognition
```

> SQLite is built-in with Python, no need to install.

### 4. Run the app

```bash
python app.py
```

### 5. Open your browser

Go to [http://localhost:2000](http://localhost:2000)  
Use the mic button to speak with MAC.

---

## 🔧 Requirements

- Python 3.7+
- Flask
- SpeechRecognition
- eSpeak (for speech output)

Install eSpeak:
```bash
sudo apt update
sudo apt install espeak
```

---

## 💬 Custom Responses

Edit the `patterns` dictionary in `app.py` to define how MAC should respond to specific phrases using regular expressions.

```python
patterns = {
    r"how are you": "I'm doing great!",
    r"hello": "Hi there!",
    r"bye": "Goodbye!"
}
```

---

## 📁 Project Structure

```
mac/
├── app.py
├── templates/
│   └── index.html
└── mac.db
```

---

## 📜 License

MIT © 2025 Alfie Terry
```

---

Let me know if you want it to include setup for Windows, Docker, systemd, or GitHub Pages hosting!
