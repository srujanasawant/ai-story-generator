# api/generate.py
from http.server import BaseHTTPRequestHandler
import json
import os
import google.generativeai as genai

# Configure Gemini API key (set this on Vercel)
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

class handler(BaseHTTPRequestHandler):
    def _set_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        # CORS: keep "*" during dev; lock this to your frontend origin later
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, Authorization")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_headers(200)

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length == 0:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Empty request body"}).encode("utf-8"))
                return

            raw = self.rfile.read(length).decode("utf-8")
            data = json.loads(raw)

            prompt = (data.get("prompt") or "").strip()
            if not prompt:
                self._set_headers(400)
                self.wfile.write(json.dumps({"error": "Prompt is required"}).encode("utf-8"))
                return

            model = genai.GenerativeModel("gemini-2.5-flash")
            resp = model.generate_content(prompt)
            story = (getattr(resp, "text", None) or "").strip()

            self._set_headers(200)
            self.wfile.write(json.dumps({"story": story}).encode("utf-8"))

        except Exception as e:
            self._set_headers(500)
            self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
