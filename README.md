# omnilex
Translate the Lex Fridman podcast into any language and listen to it on your phone. 

## How to use this
1. Go to the [transcripts archive on Lex's website](https://lexfridman.com/category/transcripts/)
2. Pick a transcript and copy the URL, e.g. "https://lexfridman.com/walter-isaacson-transcript/"
3. Then replace the url variable in podcast.py with your URL
4. Then just run podcast.py
5. To get it on your phone, you can use any sharing mechanism for an mp3 file, I like to use AirDrop.

N.B. You will need an [ElevenLabs](elevenlabs.io) API key, and a DeepL API key. Both of these services offer free tiers, but ElevenLabs free tier won't be enough to make audio from a full episode. Free text-to-speech models like [Bark](https://github.com/suno-ai/bark) are fine, but lower quality.
