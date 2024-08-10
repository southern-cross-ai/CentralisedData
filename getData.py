# import praw
#
# # Initialize the Reddit instance with your credentials
# reddit = praw.Reddit(
#     client_id="ew9nIcL6pVhWdHrhwhRj5w",
#     client_secret="s8kfXLXMmKtHuc4h4zpEbhAyyHIptg",
#     user_agent="Peanut by Any-Ear-8842",
# )
#
# # Choose the subreddit you want to crawl
# subreddit_name = "python"
# subreddit = reddit.subreddit(subreddit_name)
#
# # Number of posts to crawl
# num_posts = 10
#
# # Crawl the subreddit for the latest posts
# for post in subreddit.new(limit=num_posts):
#     print(f"Title: {post.title}")
#     print(f"Score: {post.score}")
#     print(f"URL: {post.url}")
#     print(f"Text: {post.selftext}\n")
#
#     # Crawl comments for each post
#     post.comments.replace_more(limit=0)
#     for comment in post.comments.list():
#         print(f"Comment by {comment.author}: {comment.body}\n")
#
#     print("=" * 40)

import os
import praw

# Initialize the Reddit instance with your credentials
reddit = praw.Reddit(
    client_id="ew9nIcL6pVhWdHrhwhRj5w",
    client_secret="s8kfXLXMmKtHuc4h4zpEbhAyyHIptg",
    user_agent="Peanut by Any-Ear-8842",
)

# Choose the subreddit you want to crawl
subreddit_name = "python"
subreddit = reddit.subreddit(subreddit_name)

# Directory to save the files
output_directory = "reddit_posts"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Number of posts to crawl
num_posts = 10

# Crawl the subreddit for the latest posts
for post in subreddit.new(limit=num_posts):
    # Create a filename based on the post ID
    file_name = f"{post.id}.txt"
    file_path = os.path.join(output_directory, file_name)

    with open(file_path, "w", encoding="utf-8") as file:
        # Write the post details
        file.write(f"Title: {post.title}\n")
        file.write(f"Author: {post.author}\n")
        file.write(f"Score: {post.score}\n")
        file.write(f"URL: {post.url}\n")
        file.write(f"Text: {post.selftext}\n")
        file.write(f"Number of Comments: {post.num_comments}\n")
        file.write("=" * 40 + "\n\n")

        # Crawl and write the comments for each post
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            file.write(f"Comment by {comment.author}:\n")
            file.write(comment.body + "\n")
            file.write("-" * 40 + "\n\n")

    print(f"Saved post {post.title} to {file_path}")

print("Done saving posts.")
