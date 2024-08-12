import pandas as pd
import re
import html
import json

# Read the CSV file
twitter_data = pd.read_csv('Raw_Data/Cricket Tweets/cricket_tweets.csv')

# Remove duplicates and check for NaNs
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print(f"Total number of rows: {twitter_data.shape[0]}")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

print(f"Number of null values per column:\n{twitter_data.isnull().sum(axis = 0)}")

# Keep only relevant columns
twitter_data = twitter_data[['text']]

# Remove duplicate tweets
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

# Pre-compile regular expressions for finding patterns in tweets to clean
url_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", flags=re.MULTILINE)  # Robust URL matching
mention_regex = re.compile(r"@[A-Za-z0-9]+")
multi_space_regex = re.compile(r'\s+')
multi_punct_regex = re.compile(r'([.,!?:;-><&])\s*\1+')  # Some have space in between e.g. ". . ."

print("\nCleaning data...\n")
# Clean tweets via function
def clean_tweets(tweet):
    # Remove URLs
    tweet = url_regex.sub("", tweet)
    # Remove @ sign
    tweet = mention_regex.sub("", tweet)
    # Remove hashtag sign but keep the text
    tweet = tweet.replace("#", "").replace("_", " ")
    # Replace multiple spaces with a single space
    tweet = multi_punct_regex.sub(" ", tweet)
    # Convert all named and numeric character references to their unicode
    tweet = html.unescape(tweet)
    # Remove non-ASCII Unicode characters (including emojis)
    tweet = tweet.encode("ascii", "ignore").decode()
    # Remove common multiple punctuations and replace them with a single one
    tweet = multi_punct_regex.sub(r'\1', tweet)
    return tweet.strip()

twitter_data['text'] = twitter_data['text'].apply(clean_tweets)

print("Saving cleaned data in JSON and CSV...\n")
# Save to a new JSON file
with open('Clean_Data/cricket_tweets.json', 'w') as f:
    for tweet in twitter_data['text']:
        json.dump({"tweet": tweet}, f)
        f.write('\n')

# Save the cleaned data to a new CSV file
twitter_data.to_csv('Clean_Data/cricket_tweets.csv', index=False, header=['tweet'])
