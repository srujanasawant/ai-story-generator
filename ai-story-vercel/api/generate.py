import os
import json
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def handler(request):
    try:
        body_text = request.body.decode("utf-8") if request.body else "{}"
        data = json.loads(body_text)
        prompt = data.get("prompt", "").strip()
        if not prompt:
            return {"statusCode": 400, "body": json.dumps({"error": "Prompt is required"})}

        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(prompt)

        return {
            "statusCode": 200,
            "body": json.dumps({"story": response.text})
        }

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
