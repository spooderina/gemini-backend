from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "AIzaSyC_P5Vv0XcO8SMvR3FMUh633PXvajGzflA"

@app.route("/generate", methods=["POST"])
def generate():
    user_input = request.json.get("prompt", "")

    url = f"https://generativelanguage.googleapis.com/v1beta2/models/chat-bison-001:generateContent?key={API_KEY}"

    data = {
        "contents": [{"parts": [{"text": user_input}]}]
    }

    r = requests.post(url, headers={"Content-Type": "application/json"}, json=data)
    result = r.json()

    try:
        response = result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        response = "Something went wrong."

    return jsonify({"response": response})
