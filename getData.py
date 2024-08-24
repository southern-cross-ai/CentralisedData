import requests
import json
import re
from langdetect import detect
from bs4 import BeautifulSoup

# Replace with your own API key and channel ID or search query
API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'YOUR_CHANNEL_ID'  # Use for fetching videos from a specific channel
SEARCH_QUERY = 'Perth'  # Use for fetching videos based on a search query
# Used: ACT; Canberra;

def get_video_ids_from_channel(channel_id, api_key, max_results=10):
    """Fetch video IDs from a specific YouTube channel."""
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&channelId={channel_id}&part=id&type=video&order=date&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()

    video_ids = [item['id']['videoId'] for item in data['items']]
    return video_ids


def get_video_ids_from_search(query, api_key, max_results=10):
    """Fetch video IDs based on a search query."""
    url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&q={query}&part=id&type=video&maxResults={max_results}"
    response = requests.get(url)
    data = response.json()

    video_ids = [item['id']['videoId'] for item in data['items']]
    return video_ids


def remove_emojis(text):
    """Remove emojis from the text."""
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F700-\U0001F77F"  # alchemical symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA00-\U0001FA6F"  # Chess Symbols
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002702-\U000027B0"  # Dingbats
        u"\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def is_english(text):
    """Check if text is in English"""
    try:
        return detect(text) == 'en'
    except:
        return False

def remove_html_tags(text):
    """Remove HTML tags from the text."""
    return BeautifulSoup(text, "html.parser").get_text()

def get_comments(video_id, api_key):
    """Fetch comments from a YouTube video."""
    comments = []
    url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}&maxResults=100"

    while url:
        response = requests.get(url)
        data = response.json()

        for item in data.get('items', []):
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            cleaned_comment = remove_html_tags(comment)  # Remove HTML tags
            cleaned_comment = remove_emojis(cleaned_comment)  # Clean the comment from emojis
            if is_english(cleaned_comment):
                comments.append({
                    'sentence': cleaned_comment,
                    'extra_info': ''  # Replace with actual extra info if needed
                })

        next_page_token = data.get('nextPageToken')
        if next_page_token:
            url = f"https://www.googleapis.com/youtube/v3/commentThreads?part=snippet&videoId={video_id}&key={api_key}&maxResults=100&pageToken={next_page_token}"
        else:
            url = None

    return comments


def save_comments_to_json(comments, filename='comments.json'):
    """Save the list of comments to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(comments, f, ensure_ascii=False, indent=4)


def main():
    # Fetch video IDs from the channel or search query
    # video_ids = get_video_ids_from_channel(CHANNEL_ID, API_KEY)
    # Uncomment the line below to use a search query instead
    video_ids = get_video_ids_from_search(SEARCH_QUERY, API_KEY, max_results=1000)

    all_comments = []

    for video_id in video_ids:
        print(f"Fetching comments for video ID: {video_id}")
        comments = get_comments(video_id, API_KEY)
        all_comments.extend(comments)

    print(f"Total comments fetched: {len(all_comments)}")
    filename = SEARCH_QUERY + ".json"
    save_comments_to_json(all_comments, filename)
    print(f"Comments saved to " + filename)


if __name__ == "__main__":
    main()
