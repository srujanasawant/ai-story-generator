# Steps
import os
import google.generativeai as genai

# 1. Configure the API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")
genai.configure(api_key=api_key)

# 2. Select the model
model = genai.GenerativeModel("gemini-2.5-pro")

# 3. Prompt the AI
user_prompt = input("Enter your story prompt: ").strip()

# 4. Generate Content
response = model.generate_content(f"Write a creative story based on: {user_prompt}", generation_config={'temperature': 0.85})

# 5. Output the story
print("\n--- Your Story ---\n")
print(response.text)