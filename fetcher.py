import os
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def fetch_tweets():
    # Calculate yesterday's date (24 hours ago)
    yesterday = datetime.utcnow() - timedelta(days=1)
    yesterday_date = yesterday.strftime("%Y-%m-%d")

    # Construct the final query with the date
    final_query = f"{os.getenv('SEARCH_BASE_QUERY')} since:{yesterday_date}"

    url = "https://twitter241.p.rapidapi.com/search-v3"
    querystring = {"type": "Top", "count": 20, "query": final_query}

    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": os.getenv("RAPIDAPI_HOST"),
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Debug output
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        response_json = response.json()
        # Write the full response to debug file
        import json

        with open("debug_response.json", "w", encoding="utf-8") as f:
            json.dump(response_json, f, indent=2, ensure_ascii=False)
        # Parse tweets and return the list
        return parse_tweets(response_json)
    else:
        print(f"Error Response: {response.text}")
        return None


def parse_tweets(json_data):
    """
    Deep traverse the JSON tree to find Tweet nodes and extract relevant information
    """
    tweets_list = []

    def traverse(obj):
        if isinstance(obj, dict):
            # Look for timeline entries that contain tweets
            if obj.get("__typename") == "TimelineTimelineEntry":
                content = obj.get("content", {})
                if content.get("__typename") == "TimelineTimelineItem":
                    item_content = content.get("content", {})
                    if item_content.get("__typename") == "TimelineTweet":
                        # Extract tweet data from TimelineTweet
                        tweet_data = item_content.get("tweet_results", {}).get(
                            "result", {}
                        )
                        if tweet_data and tweet_data.get("__typename") == "Tweet":
                            # Get user info
                            core_data = tweet_data.get("core", {})
                            user_results = core_data.get("user_results", {}).get(
                                "result", {}
                            )
                            user_info = (
                                user_results.get("core", {}) if user_results else {}
                            )

                            # Get tweet details
                            details = tweet_data.get("details", {})
                            counts = tweet_data.get("counts", {})

                            # 真实 JSON 结构提取逻辑
                            images = []
                            # tweet_node 是包含 core, details, media_entities 等字段的层级
                            media_entities = tweet_data.get("media_entities", [])
                            if isinstance(media_entities, list):
                                for media in media_entities:
                                    try:
                                        # 顺藤摸瓜提取 original_img_url
                                        img_url = (
                                            media.get("media_results", {})
                                            .get("result", {})
                                            .get("media_info", {})
                                            .get("original_img_url")
                                        )
                                        if img_url:
                                            images.append(img_url)
                                    except Exception:
                                        pass

                            # Extract required fields
                            author = user_info.get("screen_name", "")
                            text = details.get("full_text", "")
                            # Convert timestamp to readable date
                            timestamp_ms = details.get("created_at_ms")
                            import datetime

                            date = (
                                datetime.datetime.fromtimestamp(
                                    timestamp_ms / 1000.0
                                ).strftime("%Y-%m-%d %H:%M:%S")
                                if timestamp_ms
                                else ""
                            )
                            likes = counts.get("favorite_count", 0)
                            tweet_id = tweet_data.get("rest_id", "")
                            url = (
                                f"https://twitter.com/{author}/status/{tweet_id}"
                                if author and tweet_id
                                else ""
                            )

                            # Only add if it's a valid tweet (skip retweets for now)
                            if text and author:
                                tweet_info = {
                                    "author": author,
                                    "text": text,
                                    "date": date,
                                    "likes": likes,
                                    "url": url,
                                    "images": images,
                                }
                                tweets_list.append(tweet_info)

            # Recursively traverse all values in the dictionary
            for value in obj.values():
                if value is not None:  # Added null check
                    traverse(value)

        elif isinstance(obj, list):
            # Recursively traverse all items in the list
            for item in obj:
                if item is not None:  # Added null check
                    traverse(item)

    traverse(json_data)
    return tweets_list


if __name__ == "__main__":
    data = fetch_tweets()
    if data:
        parsed_tweets = parse_tweets(data)
        if parsed_tweets:
            print(parsed_tweets[0])  # Print only the first parsed tweet
        else:
            print("No tweets found or parsed.")
    else:
        print("Failed to fetch data from API.")
