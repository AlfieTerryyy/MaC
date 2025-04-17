from flask import Flask, request, render_template, jsonify
import os
import re
app = Flask(__name__)
patterns = {
    r"how are you": "I'm doing great!",
    r"what.*name": "I'm MAC, Mimic and Communicate.",
    r"tell me a joke": "Why did the chicken join a band? Because it had the drumsticks!",
    r"hello": "Hi there!",
    r"goodbye|bye": "Goodbye! See you soon!",
}


def get_response(text):
    for pattern, response in patterns.items():
        if re.search(pattern, text.lower()):
            return response
    return "Sorry, I didn't understand that."

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/listen', methods=['POST'])
def listen():
    data = request.get_json()
    user_text = data.get('text', '')
    response = get_response(user_text)

    print(f"User said: {user_text} | Responding with: {response}")
    os.system(f'espeak "{response}" -v en+m3 -s 135 -p 55 -a 200')

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
