# coding: UTF-8
import settings
from google import genai

GEMINI_API_KEY = settings.AP
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content_stream(
    model="gemini-2.0-flash",
    contents=["LLMの仕組みについて教えて"])
for chunk in response:
    print(chunk.text, end="")