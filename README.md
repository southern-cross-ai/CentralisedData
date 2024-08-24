# YouTube Comments Scraper

This script allows you to scrape comments from YouTube videos, clean them by removing emojis, non-English sentences, and HTML tags, and then save the cleaned comments to a JSON file. The script can fetch video IDs from a specific YouTube channel or based on a search query.

## Features

- Fetches video IDs from a specific YouTube channel or based on a search query.
- Scrapes comments from each video.
- Removes emojis, HTML tags, and non-English sentences from comments.
- Saves cleaned comments to a JSON file.

## Requirements

- Python 3.x
- `requests` library
- `langdetect` library
- `beautifulsoup4` library

## Installation

1. **Clone the repository or download the script:**

   ```bash
   git clone https://github.com/your-repository/youtube-comments-scraper.git
   cd youtube-comments-scraper
   ```

2. **Install the required Python libraries:**

   ```bash
   pip install requests langdetect beautifulsoup4
   ```

## Setup

1. **Get a YouTube Data API Key:**
   - Visit the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project and enable the YouTube Data API v3.
   - Generate an API key from the Credentials page.

2. **Edit the script:**
   - Open the `youtube_comments_to_json.py` file.
   - Replace `YOUR_API_KEY` with your YouTube Data API key.
   - Replace `YOUR_CHANNEL_ID` with the ID of the YouTube channel you want to scrape, or use a search query by uncommenting the relevant line.

## Usage

1. **Run the script:**

   ```bash
   python youtube_comments_to_json.py
   ```

2. **Output:**
   - The script will create a `comments.json` file in the same directory, containing the cleaned comments.

## Example

Here’s an example of how a comment might look before and after cleaning:

- **Original Comment:**
  ```html
  <a href="http://www.youtube.com/results?search_query=%23195challenge">#195challenge</a> Why this name?<br><br> 😊
  ```

- **Cleaned Comment:**
  ```plaintext
  #195challenge Why this name?
  ```

## How It Works

1. **Fetching Video IDs:**
   - The script can fetch video IDs from a specific channel or based on a search query.

2. **Scraping Comments:**
   - It iterates over the video IDs, making API requests to retrieve comments.

3. **Cleaning Comments:**
   - **HTML Tags:** Removed using `BeautifulSoup`.
   - **Emojis:** Removed using a regular expression.
   - **Non-English Sentences:** Filtered out using the `langdetect` library.

4. **Saving Comments:**
   - The cleaned comments are saved in a JSON file with the following structure:

   ```json
   [
       {
           "sentence": "Cleaned comment text",
           "extra_info": "This is additional info"
       },
       ...
   ]
   ```

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue.


