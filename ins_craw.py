import requests
import pandas as pd

# 替换为你的Instagram Access Token
access_token = #eg
user_id = GET https://graph.instagram.com/v20.0/me
  ?fields={fields}
  &access_token={access-token}


# 示例：获取指定标签的公开帖子
def get_posts_by_hashtag(hashtag, access_token):
    url = f"https://graph.instagram.com/ig_hashtag_search"
    params = {
        'user_id': user_id,  # 使用你自己的Instagram User ID
        'q': hashtag,
        'access_token': access_token
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        hashtag_info = response.json()
        hashtag_id = hashtag_info['data'][0]['id']

        # 获取该标签下的媒体帖子
        media_url = f"https://graph.instagram.com/{hashtag_id}/recent_media"
        media_params = {
            'user_id': 'your_user_id',
            'fields': 'id,caption,media_type,media_url,permalink,thumbnail_url,timestamp',
            'access_token': access_token
        }
        media_response = requests.get(media_url, media_params)
        if media_response.status_code == 200:
            return media_response.json().get('data', [])
        else:
            print(f"Error fetching media: {media_response.status_code}")
            return []
    else:
        print(f"Error searching hashtag: {response.status_code}")
        return []

# 保存数据到CSV
def save_posts_to_csv(posts, filename):
    if posts:
        df = pd.DataFrame(posts)
        df.to_csv(filename, index=False)
        print(f"Data saved to {filename}")
    else:
        print("No data to save")

# 示例使用
hashtag = "Australia"
posts = get_posts_by_hashtag(hashtag, access_token)
save_posts_to_csv(posts, "instagram_posts.csv")
