# How to retrieve tweets from tweet IDs using twarc

## Prerequisites

- Python installed on the machine
- Twarc installed. You can install Twarc using pip:

```sh
pip install twarc
```

## To use Twarc, you need to configure it with your Twitter API credentials. Follow these steps:
1. Create a Twitter Developer Account:
   * Go to the Twitter Developer website and sign in with your Twitter account.
   * Apply for a developer account if you don't already have one.
2. Create a Twitter App:
   * Navigate to the Twitter Developer Portal and create a new project and app.
   * Go to the "Keys and tokens" tab for your app to find your API key, API secret key, Access token, and Access token secret.
3. Run Twarc Configure:
   * Open your terminal and run:
   *   ```sh
       twarc configure
       ```
   * Enter the API key, API secret key, Access token, and Access token secret when prompted.

## Hydrate tweets
1. Create a File with Tweet IDs:
   * Save the list of tweet IDs to a text file, with each ID on a new line.
2. Hydrate the Tweets:
   * Use the hydrate command to retrieve the original tweets:
   *  ```sh
      twarc hydrate example.txt > hydrated_tweets.jsonl 
      ```
   * The tweets will be saved in a JSON Lines format file named hydrated_tweets.jsonl.
