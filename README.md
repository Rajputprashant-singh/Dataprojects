Just gemini project 

Steps to Set Up the Project
1️⃣Create a folder on the desktop
Name it something like "AI_Chatbot"
2️⃣Open VS Code
Click File → Open Folder
Select the newly created folder
3️⃣Create 3 files inside the folder:
app.py → (Put all Python backend code)
index.html → (Put all front-end code)
.env → (Store the Gemini API key)
4️⃣Generate a Gemini API key from Google:
Go to Google AI Studio
Sign in and create an API key
Copy the key and paste it into the .env file like this: 
GEMINI_API_KEY=your_api_key_here
5️⃣Open Terminal in VS Code (CMD Mode):
Click Terminal → New Terminal
Select CMD (Command Prompt)
6️⃣Install Required Libraries:
Run the following command in the terminal:
pip install python-dotenv flask google-generativeai
7️⃣Run the Python File:
python app.py
✅ Now your chatbot will be running on http://127.0.0.1:5000/
