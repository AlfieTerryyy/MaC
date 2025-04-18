from flask import Flask, request, render_template, jsonify
import os
import re
import sqlite3

app = Flask(__name__)

#--------------------- Response patterns
patterns = {
    r"\b(how are you)\b": "I'm doing great!",
    r"\b(what.*name)\b": "I'm MAC, Mimic and Communicate.",
    r"\b(tell me a joke)\b": "Why did the chicken join a band? Because it had the drumsticks!",
    r"\b(hello|hi|hallo|greetings)\b": "Greetings human!",
    r"\b(goodbye|bye)\b": "Goodbye! See you soon!",
    r"\b(love you.*)\b": "thankyou, thankyou so much, i love you too",
    r"\b(.*batman)\b": "im a night stalking crime fighting vigilante and a heavy metal rapping machine",
    r"\b(alfie terry|alfie|terry)\b": "THATS MY CREATOR!!!, i love Alfie, Alfie = father",
    r"\b(lawri darbyshire|lorry derbyshire)\b": "that's fathers smart friend",
    r"\b(linux)\b": "Good choice in OS",
    r"\b(i hate.*)\b": "Wow, hate is a strong word",
}

#--------------------- Ensure DB exists
def init_db():
    conn = sqlite3.connect("mac.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_input TEXT,
            mac_response TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_db()

def get_response(text):
    for pattern, response in patterns.items():
        if re.search(pattern, text.lower()):
            return response
    return "Sorry, I didn't understand that."

def speak(text):
    os.system(f'espeak "{text}" -v en+m3 -s 135 -p 55 -a 200')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listen', methods=['POST'])
def listen():
    data = request.get_json()
    user_text = data.get('text', '')
    response = get_response(user_text)

    #--------------------- Speak the response
    speak(response)

    #--------------------- Store in database
    conn = sqlite3.connect("mac.db")
    c = conn.cursor()
    c.execute("INSERT INTO conversations (user_input, mac_response) VALUES (?, ?)", (user_text, response))
    conn.commit()
    conn.close()

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2000, debug=True)
