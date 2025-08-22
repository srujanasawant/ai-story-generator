import json
import os
from google import genai

# Initialize the GenAI client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def handler(request):
    try:
        # Parse the incoming JSON request
        body = json.loads(request.body or "{}")
        prompt = body.get("prompt", "").strip()
        if not prompt:
            return {"statusCode": 400, "body": json.dumps({"error": "Prompt is required."})}

        # Generate content using the Gemini API
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=[prompt]
        )

        # Extract the generated story text
        story = response.text.strip()
        if not story:
            return {"statusCode": 500, "body": json.dumps({"error": "Failed to generate story."})}

        return {
            "statusCode": 200,
            "body": json.dumps({"story": story})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }