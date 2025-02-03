from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()  # Load API key from .env
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    
    # Call Gemini API
    response = model.generate_content(user_message)
    bot_reply = response.text
    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)