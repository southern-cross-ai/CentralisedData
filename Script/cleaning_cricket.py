import pandas as pd
import re
import html
import json
import os

# Read the CSV file
twitter_data = pd.read_csv('/Users/mamtagrewal/PycharmProjects/twitter/Raw_Data/Cricket Tweets/cricket_tweets.csv')

# List of major Australian cities, states, and the country name
australian_locations = [
    'Australia', 'Sydney', 'Melbourne', 'Brisbane', 'Perth', 'Adelaide', 'Gold Coast', 'Canberra', 'Newcastle',
    'Wollongong', 'Logan City', 'Geelong', 'Hobart', 'Townsville', 'Cairns', 'Darwin', 'Toowoomba',
    'Ballarat', 'Bendigo', 'Albury', 'Launceston', 'Mackay', 'Rockhampton', 'Bunbury', 'Bundaberg',
    'Sunshine Coast', 'Tasmania', 'Victoria', 'Queensland', 'New South Wales', 'South Australia',
    'Western Australia', 'Northern Territory', 'ACT'
]

# Function to check if location is in Australia
def is_australian_location(location):
    if pd.isna(location):
        return False
    for loc in australian_locations:
        if loc.lower() in location.lower():
            return True
    return False

# Calculate the total number of tweets before filtering
total_tweets = twitter_data.shape[0]

# Filter tweets to keep only those from Australian locations
twitter_data['is_australian'] = twitter_data['user_location'].apply(is_australian_location)
twitter_data = twitter_data[twitter_data['is_australian']]

# Calculate and print the percentage of tweets from Australia
australian_tweets = twitter_data.shape[0]
percentage_australian_tweets = (australian_tweets / total_tweets) * 100
print(f"Percentage of tweets from Australia: {percentage_australian_tweets:.2f}%")

# Remove duplicates and check for NaNs
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print(f"Total number of rows: {twitter_data.shape[0]}")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

print(f"Number of null values per column:\n{twitter_data.isnull().sum(axis = 0)}")

# Keep only relevant columns and rename the column to "tweet"
twitter_data = twitter_data[['text']].rename(columns={'text': 'tweet'})

# Remove duplicate tweets
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

# Pre-compile regular expressions for finding patterns in tweets to clean
url_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", flags=re.MULTILINE)  # Robust URL matching
mention_regex = re.compile(r"@[A-Za-z0-9]+")
hashtag_regex = re.compile(r"#\w+")
multi_space_regex = re.compile(r'\s+')
multi_punct_regex = re.compile(r'([.,!?:;-><&])\s*\1+')  # Some have space in between e.g. ". . ."

print("\nCleaning data...\n")
# Clean tweets via function
def clean_tweets(tweet):
    # Remove URLs
    tweet = url_regex.sub("", tweet)
    # Remove @ sign
    tweet = mention_regex.sub("", tweet)
    # Remove hashtags entirely
    tweet = hashtag_regex.sub("", tweet)
    # Replace multiple spaces with a single space
    tweet = multi_punct_regex.sub(" ", tweet)
    # Convert all named and numeric character references to their unicode
    tweet = html.unescape(tweet)
    # Remove non-ASCII Unicode characters (including emojis)
    tweet = tweet.encode("ascii", "ignore").decode()
    # Remove common multiple punctuations and replace them with a single one
    tweet = multi_punct_regex.sub(r'\1', tweet)
    return tweet.strip()

twitter_data['tweet'] = twitter_data['tweet'].apply(clean_tweets)

print("Saving cleaned data in JSON and CSV...\n")

# Save to a new CSV file
twitter_data.to_csv('cricket_tweets.csv', index=False)

# Save to a new JSON file
twitter_data.to_json('cricket_tweets.json', orient='records', lines=True)
