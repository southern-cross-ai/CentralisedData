# Reddit-Data
`
Haoqing Liu created on 10th Aug, 2024.
`
## Introduction

This script is designed to crawl data from Reddit, a popular social media and discussion platform where registered users can submit content such as links, text posts, and images. Reddit is divided into communities known as "subreddits," each focused on specific topics. Users can comment on posts, vote on content, and participate in discussions.

This Python script leverages the Reddit API via the `PRAW` (Python Reddit API Wrapper) library to extract posts and comments from a specified subreddit. The data is saved locally as text files, each representing a post and its associated comments.

## Dataset Structure

The script saves the data in a directory called `reddit_posts`. Each post is saved as a separate `.txt` file with the following structure:

- **File Naming Convention**: Each file is named after the Reddit post ID to ensure uniqueness.
- **File Content**:
  - **Title**: The title of the post.
  - **Author**: The username of the post's author.
  - **Score**: The score (upvotes minus downvotes) of the post.
  - **URL**: The direct URL to the post on Reddit.
  - **Text**: The main body text of the post.
  - **Number of Comments**: The total number of comments on the post.
  - **Comments**: Each comment is saved with the commenter's username and the comment's text, separated by a line of hyphens.

### Example of a Saved File:

```
Title: How to learn Python?
Author: example_user
Score: 125
URL: https://www.reddit.com/r/python/comments/xxxxxx/how_to_learn_python/
Text: I'm new to programming and want to learn Python. Any suggestions?
Number of Comments: 23
========================================

Comment by user1:
I recommend starting with the official Python documentation.
----------------------------------------

Comment by user2:
Try some online courses like Coursera or edX.
----------------------------------------
```

## How to Run the Script

### Prerequisites

Before running the script, ensure you have the following installed:

- **Python**: Version 3.6 or higher.
- **PRAW**: Install via pip using the command `pip install praw`.

### Setup

1. **Reddit API Credentials**: 
   - Create a Reddit account if you don't have one.
   - Go to [Reddit's App Preferences](https://www.reddit.com/prefs/apps) and create a new application with type "script."
   - Note down your `client_id`, `client_secret`, and `user_agent`.

2. **Script Configuration**:
   - Open the `getData.py` script in a text editor.
   - Replace the placeholder values `YOUR_CLIENT_ID`, `YOUR_CLIENT_SECRET`, and `YOUR_USER_AGENT` with your Reddit API credentials.

3. **Subreddit Selection**:
   - In the script, modify the `subreddit_name` variable to the subreddit you wish to crawl (e.g., "python", "datascience").

### Running the Script

1. **Run the Script**:
   - Open a terminal and navigate to the directory containing `getData.py`.
   - Run the script using Python:

   ```bash
   python getData.py
   ```

2. **Check the Output**:
   - After running the script, a directory named `reddit_posts` will be created (if it doesn't already exist).
   - The script will save the posts and comments as `.txt` files in this directory.

### Notes

- **Error Handling**: Ensure that the Reddit API credentials are correct. Incorrect credentials will result in an authentication error.
- **Rate Limits**: Reddit's API enforces rate limits. Be mindful of the number of requests made in a short period to avoid being blocked.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

