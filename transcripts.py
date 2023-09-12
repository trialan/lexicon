import requests
from bs4 import BeautifulSoup


def get_transcript(url):
    soup = fetch_web_page(url)
    transcript_divs = get_transcript_segments(soup)

    current_speaker = None
    current_text = ""
    formatted_transcript = []

    for div in transcript_divs:
        speaker, text = extract_speaker_and_text(div)
        if not speaker:
            speaker = current_speaker
        if not current_speaker:
            current_speaker = speaker
        if speaker == current_speaker:
            current_text += f" {text}"
        else:
            append_to_transcript(formatted_transcript, current_speaker, current_text)
            current_speaker = speaker
            current_text = text
    append_to_transcript(formatted_transcript, current_speaker, current_text)
    return formatted_transcript


def fetch_web_page(url):
    response = requests.get(url)
    assert response.status_code == 200
    return BeautifulSoup(response.content, 'html.parser')


def get_transcript_segments(soup):
    return soup.find_all('div', {'class': 'ts-segment'})


def extract_speaker_and_text(div):
    speaker = div.find('span', {'class': 'ts-name'})
    text = div.find('span', {'class': 'ts-text'})
    return (speaker.text if speaker else None, text.text if text else "")


def append_to_transcript(formatted_transcript, current_speaker, current_text):
    formatted_transcript.append(f"{current_speaker}: {current_text.strip()}")


if __name__ == '__main__':
    url = 'https://lexfridman.com/walter-isaacson-transcript/'
    transcript = get_transcript(url)

