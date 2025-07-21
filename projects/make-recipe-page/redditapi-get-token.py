# Demonstrate how you can log in to the Reddit API to receive content that
# requires authentication, using only `requests` and your credentials.

import requests
import pprint

import requests.auth

# Rplace with actual credentials 
client_id = "ur_client_id"
client_secret = "ur_client_secret"
username = "ur_reddit_username"
password = "ur_reddit_password"

# Get acces tokem
auth = requests.auth.HTTPBasicAuth(client_id, client_secret)

data = {
    "grant_type": "password",
    "username": username,
    "password": password,

}

headers = {
    "User-Agent": "MyRedditApp/0.1 by 'ur_username'"
}

response = requests.post("https://www.reddit.com/api/v1/access_token",
                         auth=auth, data=data, headers=headers)

if response.status_code != 200:
    print("Failed to get token", response.text)
    exit()

token = response.json()["access.token"]
print("Access token obtained")

# Use token to access reddit
headers["Authorization"] = f"bearer{token}"

# example
res = requests.get("https://oauth.reddit.com/best", headers=headers)

if res.status_code == 200:
    print("Authenticated content:")
    pprint.pprint(res.json()['data']['children'][:3])  # Show top 3 posts
else:
    print("Failed to access content:", res.text)