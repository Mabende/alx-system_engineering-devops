#!/usr/bin/python3
"""
Contains the number_of_subscribers function
"""
import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the
        subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str) or \
       not subreddit.isidentifier():
        return 0

    try:
        response = requests.get(
            'http://www.reddit.com/r/{}/about.json'.format(subreddit),
            headers={'User-Agent': '0x16-api_advanced:v1.0.0 (by /u/firdaus_cartoon_jr)'}
        )

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'subscribers' in data['data']:
                return data['data']['subscribers']

    except requests.RequestException as e:
        print("An error occurred: ", e)

    return 0
