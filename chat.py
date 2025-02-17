# coding: UTF-8
import settings
from google import genai

GEMINI_API_KEY = settings.AP
client = genai.Client(api_key=GEMINI_API_KEY)

chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message("生成AIを活用した実装案を考えてください")
print(response.text)
response = chat.send_message("ファインチューニングとは何ですか？")
print(response.text)
for message in chat._curated_history:
    print(f'role - ', message.role, end=": ")
    print(message.parts[0].text)