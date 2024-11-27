# Sentiment Analysis on Tweets

## Description

This project performs sentiment analysis on tweets using the Twitter API v2 and NLTK's SentimentIntensityAnalyzer. It collects recent tweets on a specific topic, preprocesses the tweets, performs sentiment analysis, and visualizes the sentiment distribution using a pie chart.

## Key Features

- **Twitter API v2 Integration**: Collects tweets using Twitter's API v2.
- **Sentiment Analysis**: Analyzes the sentiment of the collected tweets (positive, negative, neutral).
- **Visualization**: Displays a pie chart representing the sentiment distribution.
- **Error Handling**: Handles rate limits and API errors gracefully.

## Advantages

- **Real-Time Data**: Gathers and analyzes live tweets.
- **Easy to Use**: Simple Python script with clear outputs.
- **Customizable**: Modify the query to analyze different topics or hashtags.
- **Insightful Results**: Provides an overview of sentiment trends for a given topic.

## Requirements

Before running the script, make sure you have the following Python packages installed:

- `tweepy`
- `pandas`
- `nltk`
- `matplotlib`
- `python-dotenv`

You can install all the required packages via `requirements.txt`:

```bash
pip install -r requirements.txt
```

### `requirements.txt`
```text
tweepy
pandas
nltk
matplotlib
python-dotenv
```

## Installation

1. Clone the repository or download the code files.
   ```bash
   git clone https://github.com/Nabegh-Anane/Sentiment-Analysis-on-Tweets.git
   cd Sentiment-Analysis-on-Tweets
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your Twitter Developer credentials:
   - Follow the steps below to get your Twitter API credentials.
   - Create a `.env` file and add your API credentials as follows:
     ```
        CONSUMER_KEY=your_consumer_key
        CONSUMER_SECRET=your_consumer_secret
        ACCESS_TOKEN=your_access_token
        ACCESS_TOKEN_SECRET=your_access_token_secret
        BEARER_TOKEN=your_bearer_token_here
     ```

## Usage

1. Download and install `vader_lexicon`, run the script:
   ```bash
   python vader_lexicon.py
   ```

2. After setting up your credentials, run the script:
   ```bash
   python SentimentIntensityAnalyzer.py
   ```

3. The script will collect recent tweets on the topic `"Python programming"`, perform sentiment analysis, and generate a pie chart visualizing the sentiment distribution.

## Example

Here’s an example of how the output will look:

![Sentiment Distribution](https://nabeghanane-portfolio.imgix.net/assets/projects/output/Sentiment-Analysis-on-Tweets.png)

## Future Improvements

- **Expanded Analysis**: Incorporate more advanced sentiment analysis models like BERT or GPT.
- **Data Storage**: Store the collected tweets and sentiment analysis results in a database.
- **Real-Time Tracking**: Implement a real-time tracking system for ongoing sentiment analysis.
- **Multilingual Support**: Support for analyzing tweets in multiple languages.

## Common Steps to Get Twitter API Credentials

To get your own Twitter API credentials, follow these steps:

### Step 1: Create a Twitter Developer Account
- Go to the [Twitter Developer Portal 'X Developer Now'](https://developer.x.com/) and log in with your Twitter account.
- Apply for a developer account if you don't have one. This process includes answering a few questions about how you intend to use the API.

![Step 1](https://nabeghanane-portfolio.imgix.net/assets/projects/output/stepsAPITwitter/step1.png)

### Step 2: Create a New Twitter App
- After approval, go to the "Projects & Apps" section and create a new project and app.

![Step 2](https://nabeghanane-portfolio.imgix.net/assets/projects/output/stepsAPITwitter/step2.png)

### Step 3: Access API Keys and Tokens
- Once your app is created, go to the "Keys and Tokens" section to access your API keys.

![Step 3](https://nabeghanane-portfolio.imgix.net/assets/projects/output/stepsAPITwitter/step3.png)

### Step 4: Generate Your Bearer Token
- In the "Keys and Tokens" section, generate the Bearer Token that you will use to authenticate with the Twitter API.

![Step 4](https://nabeghanane-portfolio.imgix.net/assets/projects/output/stepsAPITwitter/step4.png)

### Step 5: Add Credentials to `.env` File
- After retrieving the credentials (Bearer Token), create a `.env` file in your project directory and add your Bearer Token like this:
  ```
   CONSUMER_KEY is the API Key in the Consumer Keys of the APP Tokens 
   CONSUMER_SECRET is the API Key Secret in the Consumer Keys of the APP Tokens 
   ACCESS_TOKEN is the Access Token in the Authentication Tokens of the APP Tokens 
   ACCESS_TOKEN_SECRET is the Access Token Secret in the Authentication Tokens of the APP Tokens 
   BEARER_TOKEN is the Bearer Token in the Authentication Tokens of the APP Tokens 
  ```

![Step 5](https://nabeghanane-portfolio.imgix.net/assets/projects/output/stepsAPITwitter/step5.png)

### Execution GIF & Output Image:
These are referenced with URLs as per your provided links:
- **Execution GIF**: [Sentiment Analysis GIF](https://nabeghanane-portfolio.imgix.net/assets/projects/output/Sentiment-Analysis-on-Tweets.gif)


Ensure the `.env` file with your credentials is correctly set up before running the script.

## Author

**Nabegh Anane**

Visit my [Portfolio](https://nabeghanane.com/) for more projects and information.