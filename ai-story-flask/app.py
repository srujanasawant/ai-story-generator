from flask import Flask, render_template, request, jsonify
import google.generativeai as genai    # not API itself but a wrapper # REST API
import os
from dotenv import load_dotenv

# Set GEMINI_API_KEY as environment variable
# Load environment variable
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Configure this program as a flask object
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate_story():
    data = request.get_json()
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error: Prompt is required"}), 400
    
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(prompt)

    return jsonify({"story": response.text})

if __name__ == "__main__":
    app.run(debug=True)