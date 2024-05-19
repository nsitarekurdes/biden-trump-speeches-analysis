# Biden and Trump's Speeches on Israel-Gaza Conflict

## Introduction
This project analyzes speeches and statements made by President Joe Biden and former President Donald Trump regarding the Israel-Gaza conflict from October 2023 to January 2024.

## Methodology
### Data Collection
Speeches were collected from the following official websites and news outlets:
- **Biden's Speeches**: [White House](https://www.whitehouse.gov), [CNN](https://edition.cnn.com), [Reuters](https://www.reuters.com)
- **Trump's Speeches**: [AA](https://www.aa.com.tr), [Times of Israel](https://www.timesofisrael.com), [NBC News](https://www.nbcnews.com)

### Data Processing
The collected speeches were analyzed for sentiment using the TextBlob library, which provides a simple API for diving into common natural language processing (NLP) tasks.

### Steps:
1. **Scraping Speeches**: The `scrape_speech` function uses the `requests` library to fetch the web pages and `BeautifulSoup` to parse the HTML content.
2. **Sentiment Analysis**: The `analyze_sentiment` function uses `TextBlob` to perform sentiment analysis on the speeches. The sentiment analysis provides insights into the polarity (positive or negative) and subjectivity (objective or subjective) of each speech.
3. **Saving Results**: The results are saved in a JSON file for further analysis and reporting.

## Requirements
The project requires the following Python libraries:
- `requests`: For making HTTP requests to fetch web pages.
- `beautifulsoup4`: For parsing HTML content.
- `textblob`: For performing sentiment analysis.

Install the dependencies using:
```sh
pip install -r requirements.txt
