#!/usr/bin/python3
"""Contains recurse function"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    if hot_list is None:
        hot_list = []
    
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "0x16-api_advanced:project:v1.0.0 (by /u/firdaus_cartoon_jr)"
    }
    params = {
        "after": after,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if response.status_code != 200:
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    children = results.get("children", [])
    
    for child in children:
        hot_list.append(child.get("data", {}).get("title", ""))
    
    if after:
        return recurse(subreddit, hot_list, after)
    
    return hot_list
