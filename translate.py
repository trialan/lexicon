import os
import requests
import json

API_KEY = os.environ.get('DEEPL_API_KEY')

def translate_to_spanish(text):
    url = "https://api-free.deepl.com/v2/translate"
    params = {
        'auth_key': API_KEY,
        'text': text,
        'target_lang': 'ES'
    }
    response = requests.post(url, data=params)
    translation_data = json.loads(response.text)
    translated_text = translation_data['translations'][0]['text']
    return translated_text


