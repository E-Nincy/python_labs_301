# Using the external `praw` package, fetch recipes through the Reddit API
# and re-build the CodingNomads recipe collection website.
# If you commit this code to GitHub, make sure to keep your API secrets
# out of version control, for example by adding them as environment variables.

import os
import praw
from dotenv import load_dotenv

load_dotenv()  # optional, if using a .env file

# Initialize Reddit instance
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT")  # e.g., "RecipeScraper/0.1 by your_username"
)

# Choose a subreddit related to recipes
subreddit = reddit.subreddit("recipes")

# Fetch top 10 recipes from the week
recipes = []

for post in subreddit.top(limit=10, time_filter='week'):
    recipes.append({
        "title": post.title,
        "url": post.url,
        "score": post.score,
        "comments": post.num_comments,
        "permalink": f"https://www.reddit.com{post.permalink}"
    })

# Display the recipes
for i, recipe in enumerate(recipes, 1):
    print(f"{i}. {recipe['title']} ({recipe['score']} upvotes)")
    print(f"URL: {recipe['url']}")
    print(f"Reddit Thread: {recipe['permalink']}")
    print(f"Comments: {recipe['comments']}\n")

