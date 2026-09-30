from google import genai

from app.config import settings


api_key = settings.gemini_api_key.strip()

if not api_key:
    raise RuntimeError("GEMINI_API_KEY was not loaded")

print("Gemini API key loaded: True")
print("Key length:", len(api_key))

client = genai.Client(
    api_key=api_key
)

response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents="Reply with exactly: Gemini connection successful.",
)

print("Gemini response:")
print(response.text)
