# 🎙️ MAC — Mimic and Communicate
## ~ Windows version not tested and under construction

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

```
MIT License

Copyright (c) 2025 Alfie Terry

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
