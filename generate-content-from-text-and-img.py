# coding: UTF-8
import settings
from google import genai
from PIL import Image

GEMINI_API_KEY = settings.AP

client = genai.Client(api_key=GEMINI_API_KEY)

image = Image.open("./img/cat.jpg")
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[image, "この猫について教えてください"])
print(response.text)