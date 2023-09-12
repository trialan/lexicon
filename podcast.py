from lexicon.speech import generate_podcast_file
from lexicon.transcripts import get_transcript
from lexicon.translate import translate_to_spanish

if __name__ == '__main__':
    url = "https://lexfridman.com/walter-isaacson-transcript/"
    transcript = get_transcript(url)
    print("Translating ...")
    translated_transcript = [translate_to_spanish(s) for s in transcript]
    print("Generating audio file ...")
    generate_podcast_file(translated_transcript, "trial-walter-isaacson-v3")

