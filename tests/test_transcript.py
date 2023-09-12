from lexicon.transcripts import get_transcript

def test_getting_full_transcript():
    url = "https://lexfridman.com/walter-isaacson-transcript/"
    transcript = get_transcript(url)
    assert_transcript_is_correct(transcript)

def assert_transcript_is_correct(transcript):
    assert last_word_in_string(transcript[0]) == "it."
    assert last_word_in_string(transcript[1]) == "fate?"
    assert last_word_in_string(transcript[2]) == "do."
    assert last_word_in_string(transcript[3]) == "learned?"
    assert last_word_in_string(transcript[4]) == "him."
    assert last_word_in_string(transcript[-1]) == "time."


def last_word_in_string(s):
    return s.split(' ')[-1]
