import os
import requests
import numpy as np
from pydub import AudioSegment
import soundfile as sf
from tqdm import tqdm

API_KEY = os.environ.get('XI_API_KEY')

CHUNK_SIZE = 1024
LEX_VOICE = "https://api.elevenlabs.io/v1/text-to-speech/pNInz6obpgDQGcFmaJgB"
GUEST_VOICE = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": API_KEY
}

data = {
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

lex_guitar = "audio_files/lex_guitar_segment.mp3"


def generate_podcast_file(transcript, filename):
    all_audio_data = []

    for i, text in tqdm(enumerate(transcript)):
        voice = LEX_VOICE if i % 2 == 1 else GUEST_VOICE
        speech_response = _get_speech(text, voice)
        temp_filename = f"audio_files/temp/{filename}_temp_{i}.wav"
        _save_speech(speech_response, temp_filename)
        audio_data, sample_rate = sf.read(temp_filename)
        all_audio_data.append(audio_data)

    final_audio_data = np.concatenate(all_audio_data)
    path = f'audio_files/{filename}.mp3'
    sf.write(path, final_audio_data, sample_rate)
    _add_guitar_at_start_and_end_of_podcast(path)


def _add_guitar_at_start_and_end_of_podcast(path):
    _append_audio_files(path, lex_guitar, path)
    _append_audio_files(lex_guitar, path, path)


def _append_audio_files(main_file, append_file, output_file):
    main_audio = AudioSegment.from_mp3(main_file)
    append_audio = AudioSegment.from_mp3(append_file)
    final_audio = append_audio + main_audio + append_audio
    final_audio.export(output_file, format="mp3")


def _get_speech(text, voice):
    response = requests.post(voice, json={**data, "text": text}, headers=headers)
    return response


def _save_speech(speech, filename):
    with open(filename, 'wb') as f:
        for chunk in speech.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)


if __name__ == '__main__':
    conversation = [
        "Hola chico, como estas hoy?",
        "Muy bien, y tu Felipe? Como te sientes?"
    ]
    generate_podcast_file(conversation)
