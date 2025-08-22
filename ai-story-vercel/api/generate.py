import os
import json
import google.generativeai as genai

# Vercel serverless function handler
def handler(request, response):
    try:
        # Parse request body
        body = request.get_json()
        prompt = body.get("prompt", "")

        if not prompt:
            response.status_code = 400
            response.send(json.dumps({"error": "Prompt is required"}))
            return

        # Configure Gemini
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])
        model = genai.GenerativeModel("gemini-2.5-flash")
        result = model.generate_content(prompt)

        # Return story
        response.status_code = 200
        response.headers["Content-Type"] = "application/json"
        response.send(json.dumps({"story": result.text}))

    except Exception as e:
        response.status_code = 500
        response.send(json.dumps({"error": str(e)}))
