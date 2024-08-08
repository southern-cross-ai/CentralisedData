import pandas as pd
import re

# Path to the CSV file
file_path = '/auspol2019.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

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
            recognized_australian_locations.append(location)
            return True
    return False

# Function to clean tweets by removing links, hashtags, and emojis
def clean_tweet(tweet):
    tweet = re.sub(r"http\S+|www\S+|https\S+", '', tweet, flags=re.MULTILINE)  # Remove URLs
    tweet = re.sub(r'#\w+', '', tweet)  # Remove hashtags
    tweet = re.sub(r'[^\w\s,]', '', tweet)  # Remove emojis and other non-word characters
    tweet = re.sub(r'\s+', ' ', tweet).strip()  # Remove extra whitespace
    return tweet

# List to store recognized Australian locations
recognized_australian_locations = []

# Apply the function to the DataFrame
df['is_australian'] = df['user_location'].apply(is_australian_location)

# Filter the DataFrame to include only Australian tweets
australian_tweets_df = df[df['is_australian']].copy()

# Clean the tweets
australian_tweets_df.loc[:, 'cleaned_full_text'] = australian_tweets_df['full_text'].apply(clean_tweet)

# Create a new DataFrame with only one column for the cleaned tweets
cleaned_tweets_df = australian_tweets_df[['cleaned_full_text']].rename(columns={'cleaned_full_text': 'tweet'})

# Save to a new CSV file
cleaned_tweets_df.to_csv('auspol2019.csv', index=False)

# Save to a new JSON file
cleaned_tweets_df.to_json('auspol2019.json', orient='records', lines=True)

print("CSV and JSON files with cleaned Australian tweets created successfully.")
