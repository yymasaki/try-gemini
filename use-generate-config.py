# coding: UTF-8
import settings
from google import genai
from google.genai import types

GEMINI_API_KEY = settings.AP
client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["生成AIを活用したサービスの実装案を考えてください"],
    config=types.GenerateContentConfig(
        max_output_tokens=500,
        temperature=0.1
    )
)
print(response.text)