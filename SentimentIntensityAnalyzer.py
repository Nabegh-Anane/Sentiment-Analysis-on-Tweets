import tweepy
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import time

# Load credentials from .env file
load_dotenv()

# Retrieve the Bearer Token from the environment variable
bearer_token = os.getenv('BEARER_TOKEN')

# Check if Bearer Token is loaded correctly
if not bearer_token:
    raise ValueError("BEARER_TOKEN not found in .env file")

# Authenticate with Twitter API v2 using the Bearer Token
client = tweepy.Client(bearer_token=bearer_token)

# Collect tweets using Tweepy API v2
def collect_tweets(query, count=100):
    try:
        tweets = client.search_recent_tweets(query=query, max_results=count, tweet_fields=["text"])
        if not tweets.data:
            return []  # Return empty list if no tweets are found
        tweet_data = [tweet.text for tweet in tweets.data]
        return tweet_data
    except tweepy.errors.TooManyRequests as e:
        print("Rate limit exceeded. Waiting for 15 minutes before retrying.")
        time.sleep(15 * 60)  # Sleep for 15 minutes before retrying
        return collect_tweets(query, count)  # Retry the request after waiting
    except Exception as e:
        print(f"Error collecting tweets: {e}")
        return []

# Preprocess and clean the tweets
def preprocess_tweets(tweets):
    clean_tweets = []
    for tweet in tweets:
        tweet = tweet.lower()
        tweet = ''.join([char for char in tweet if char.isalnum() or char.isspace()])
        clean_tweets.append(tweet)
    return clean_tweets

# Sentiment Analysis using NLTK
def analyze_sentiment(tweets):
    sia = SentimentIntensityAnalyzer()
    sentiment_labels = []
    for tweet in tweets:
        sentiment_score = sia.polarity_scores(tweet)['compound']
        if sentiment_score >= 0.05:
            sentiment_labels.append('positive')
        elif sentiment_score <= -0.05:
            sentiment_labels.append('negative')
        else:
            sentiment_labels.append('neutral')
    return sentiment_labels

# Visualize sentiment distribution
def visualize_sentiment(sentiment_labels):
    sentiment_counts = pd.Series(sentiment_labels).value_counts()
    sentiment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, figsize=(7, 7), cmap='Set3')
    plt.title('Sentiment Distribution of Tweets')
    plt.ylabel('')
    plt.show()

# Main Execution
if __name__ == "__main__":
    query = "Python programming"
    tweet_count = 100
    tweets = collect_tweets(query, tweet_count)
    
    # Proceed only if tweets were collected
    if tweets:
        preprocessed_tweets = preprocess_tweets(tweets)
        sentiment_labels = analyze_sentiment(preprocessed_tweets)
        visualize_sentiment(sentiment_labels)
    else:
        print("No tweets found or failed to collect tweets.")
