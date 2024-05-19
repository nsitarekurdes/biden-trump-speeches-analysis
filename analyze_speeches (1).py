
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import json

def scrape_speech(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        speech_text = "

".join([para.get_text(strip=True) for para in paragraphs])
        return speech_text
    else:
        print(f"Failed to retrieve the page: {url}")
        return ""

def analyze_sentiment(speeches):
    sentiments = []
    for speech in speeches:
        blob = TextBlob(speech)
        sentiment = blob.sentiment
        sentiments.append(sentiment)
    return sentiments

with open('biden_speeches.txt', 'r', encoding='utf-8') as file:
    biden_speeches = file.read().split('

')

with open('trump_speeches.txt', 'r', encoding='utf-8') as file:
    trump_speeches = file.read().split('

')

biden_sentiments = analyze_sentiment(biden_speeches)
trump_sentiments = analyze_sentiment(trump_speeches)

results = {
    "biden_sentiments": [s._asdict() for s in biden_sentiments],
    "trump_sentiments": [s._asdict() for s in trump_sentiments]
}

with open('sentiment_analysis_results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, ensure_ascii=False, indent=4)

print("Sentiment analysis results have been saved.")
