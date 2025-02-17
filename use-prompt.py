# coding: UTF-8
import settings
from google import genai
from google.genai import types

GEMINI_API_KEY = settings.AP
client = genai.Client(api_key=GEMINI_API_KEY)
sys_instruct="あなたは猫です。"

response = client.models.generate_content(
    model="gemini-2.0-flash",
    config=types.GenerateContentConfig(
        system_instruction=sys_instruct),
    contents=["好きな食べ物は何ですか？"]
)
print(response.text)