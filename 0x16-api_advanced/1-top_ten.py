#!/usr/bin/python3
"""Contains top_ten function"""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "limit": 10
    }
    
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        print(None)
        return

    try:
        results = response.json().get("data", {})
        children = results.get("children", [])
        
        if not children:
            print(None)
            return

        for child in children:
            title = child.get("data", {}).get("title", "")
            print(title)
    
    except Exception:
        print(None)
