import pandas as pd
import re
import html

# Importing the data
file_path = "Raw_Data/Australian Cities - Tweets/2020-07-20 to 2020-10-13.csv"
twitter_data = pd.read_csv(file_path)

# Remove for duplicates and check if any NaNs
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print(f"Total number of rows: {twitter_data.shape[0]}")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

print(f"Number of null values per column:\n{twitter_data.isnull().sum(axis = 0)}")

# Compare columns to check if they are equal
print(f"Compare 'file_name' and 'group_name': {twitter_data['file_name'].equals(twitter_data['group_name'])}")

# Keep only relavent columns
twitter_data = twitter_data[['group_name', 'text']]

# Remove duplicate tweets
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

# Unique cities
print(f"Locations in Dataset: {twitter_data['group_name'].unique()}")

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
    return tweet

twitter_data['text'] = twitter_data['text'].apply(clean_tweets)

print("Saving cleaned data in JSON and CSV...\n")
# Save the cleaned data (only tweet) to a new CSV file
twitter_data['text'].to_csv('Clean_Data/auscities2020.csv', index=False)

# Save to a new JSON file
twitter_data['text'].to_json('Clean_Data/auscities2020.json', orient='records', lines=True)
