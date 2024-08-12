import os
import praw

"""
Get data from Reddit
Here we only take the pure texts, without any extra information for the posts

Haoqing Liu
12 Aug 2024
"""

# Initialize the Reddit instance with your credentials
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    user_agent="USER_AGENT",
)

# Choose the subreddit you want to crawl
subreddit_name = "Australia"
subreddit = reddit.subreddit(subreddit_name)

# Directory to save the files
output_directory = "reddit_posts"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Number of posts to crawl
num_posts = 500

# Crawl the subreddit for the latest posts
for post in subreddit.new(limit=num_posts):
    # Create a filename based on the post ID
    file_name = f"{post.id}.txt"
    # it may occur an error if I change filename to post.title
    # file_name = f"{post.title}.txt"
    file_path = os.path.join(output_directory, file_name)

    # to save the whole post and all the comments:
    # with open(file_path, "w", encoding="utf-8") as file:
    #     # Write the post details
    #     file.write(f"Title: {post.title}\n")
    #     file.write(f"Author: {post.author}\n")
    #     file.write(f"Score: {post.score}\n")
    #     file.write(f"URL: {post.url}\n")
    #     file.write(f"Text: {post.selftext}\n")
    #     file.write(f"Number of Comments: {post.num_comments}\n")
    #     file.write("=" * 40 + "\n\n")
    #
    #     # Crawl and write the comments for each post
    #     post.comments.replace_more(limit=0)
    #     for comment in post.comments.list():
    #         file.write(f"Comment by {comment.author}:\n")
    #         file.write(comment.body + "\n")
    #         file.write("-" * 40 + "\n\n")

    # to save pure texts
    with open(file_path, "w", encoding="utf-8") as file:
        # Write the post details
        file.write(f"{post.selftext}\n")
        # Crawl and write the comments for each post
        post.comments.replace_more(limit=0)
        for comment in post.comments.list():
            # file.write(f"Comment by {comment.author}:\n")
            file.write(comment.body + "\n")
            # file.write("-" * 40 + "\n\n")

    print(f"Saved post {post.title} to {file_path}")

print("Done saving posts.")
