import pandas as pd
import re
import html

# Importing the data
file_path = "/Users/mamtagrewal/PycharmProjects/twitter/Raw_Data/Australian Cities - Tweets/2020-07-20 to 2020-10-13.csv"
twitter_data = pd.read_csv(file_path)

# Remove for duplicates and check if any NaNs
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print(f"Total number of rows: {twitter_data.shape[0]}")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

print(f"Number of null values per column:\n{twitter_data.isnull().sum(axis = 0)}")

# Compare columns to check if they are equal
print(f"Compare 'file_name' and 'group_name': {twitter_data['file_name'].equals(twitter_data['group_name'])}")

# Keep only relevant columns (replace 'user_location' with 'location')
twitter_data = twitter_data[['group_name', 'text', 'location']]

# Remove duplicate tweets
print(f"Total duplicated rows: {sum(twitter_data.duplicated())}, Percentage duplicates: {sum(twitter_data.duplicated())/twitter_data.shape[0]*100}%")
print("Remove all duplicates")
twitter_data.drop_duplicates(inplace=True)

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

# Apply the function to filter only Australian tweets
twitter_data['is_australian'] = twitter_data['location'].apply(is_australian_location)
australian_tweets_df = twitter_data[twitter_data['is_australian']].copy()

# Pre-compile regular expressions for finding patterns in tweets to clean
url_regex = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", flags=re.MULTILINE)  # Robust URL matching
mention_regex = re.compile(r"@[A-Za-z0-9_]+")  # Regex to match the entire @username
hashtag_regex = re.compile(r"#\w+")  # Regex to match the entire hashtag word
multi_space_regex = re.compile(r'\s+')
multi_punct_regex = re.compile(r'([.,!?:;-><&])\s*\1+')  # Some have space in between e.g. ". . ."

print("\nCleaning data...\n")
# Clean tweets via function
def clean_tweets(tweet):
    # Remove URLs
    tweet = url_regex.sub("", tweet)
    # Remove entire @username
    tweet = mention_regex.sub("", tweet)
    # Remove entire #hashtag
    tweet = hashtag_regex.sub("", tweet)
    # Replace multiple spaces with a single space
    tweet = multi_punct_regex.sub(" ", tweet)
    # Convert all named and numeric character references to their unicode
    tweet = html.unescape(tweet)
    # Remove non-ASCII Unicode characters (including emojis)
    tweet = tweet.encode("ascii", "ignore").decode()
    # Remove common multiple punctuations and replace them with a single one
    tweet = multi_punct_regex.sub(r'\1', tweet)
    return tweet

australian_tweets_df['text'] = australian_tweets_df['text'].apply(clean_tweets)

# Rename 'text' column to 'tweet' for saving
australian_tweets_df = australian_tweets_df.rename(columns={'text': 'tweet'})

print("Saving cleaned data in JSON and CSV...\n")
# Save the cleaned data (only tweet) to a new CSV file
australian_tweets_df[['tweet']].to_csv('auscities2020.csv', index=False)

# Save to a new JSON file
australian_tweets_df[['tweet']].to_json('auscities2020.json', orient='records', lines=True)
