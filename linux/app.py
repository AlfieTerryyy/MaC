from flask import Flask, request, render_template, jsonify
import os
import re
import sqlite3

app = Flask(__name__)

#--------------------- Response patterns
patterns = {
    r"how are you": "I'm doing great!",
    r"what.*name": "I'm MAC, Mimic and Communicate.",
    r"tell me a joke": "Why did the chicken join a band? Because it had the drumsticks!",
    r"hello": "Hi there!",
    r"goodbye|bye": "Goodbye! See you soon!",
    r"love you.*": "thankyou, thankyou so much, i love you too",
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
