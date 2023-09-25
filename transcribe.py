#Use the Whisper API: costs $0.006/minute of audio

import os
import openai


openai.api_key = os.getenv("OPENAI_API_KEY")


if __name__ == '__main__':
    audio_file = open("audio_files/barron.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
