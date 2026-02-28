import os
import json
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

    print(f"Query would be: {final_query}")

    # Mock response for testing purposes
    mock_response = {
        "data": {
            "search_by_raw_query": {
                "search_timeline": {
                    "timeline": {
                        "instructions": [
                            {
                                "__typename": "TimelineAddEntries",
                                "entries": [
                                    {
                                        "__typename": "TimelineTweet",
                                        "itemContent": {
                                            "__typename": "Tweet",
                                            "tweet_results": {
                                                "result": {
                                                    "__typename": "Tweet",
                                                    "core": {
                                                        "user_results": {
                                                            "result": {
                                                                "legacy": {
                                                                    "screen_name": "TechCrunch",
                                                                    "name": "TechCrunch",
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "legacy": {
                                                        "full_text": "Exciting developments in AI today with new breakthroughs in machine learning models that promise to revolutionize the industry.",
                                                        "created_at": "2023-05-15T10:30:00.000Z",
                                                        "favorite_count": 1250,
                                                        "id_str": "1234567890123456789",
                                                    },
                                                }
                                            },
                                        },
                                    },
                                    {
                                        "__typename": "TimelineTweet",
                                        "itemContent": {
                                            "__typename": "Tweet",
                                            "tweet_results": {
                                                "result": {
                                                    "__typename": "Tweet",
                                                    "core": {
                                                        "user_results": {
                                                            "result": {
                                                                "legacy": {
                                                                    "screen_name": "elonmusk",
                                                                    "name": "Elon Musk",
                                                                }
                                                            }
                                                        }
                                                    },
                                                    "legacy": {
                                                        "full_text": "Just launched another satellite to expand our global internet coverage. The future is looking bright! 🚀",
                                                        "created_at": "2023-05-15T09:15:00.000Z",
                                                        "favorite_count": 25000,
                                                        "id_str": "9876543210987654321",
                                                    },
                                                }
                                            },
                                        },
                                    },
                                ],
                            }
                        ]
                    }
                }
            }
        }
    }

    return mock_response


def parse_tweets(json_data):
    """
    Deep traverse the JSON tree to find Tweet nodes and extract relevant information
    """
    tweets_list = []

    def traverse(obj):
        if isinstance(obj, dict):
            # Check if this is a Tweet object with the actual structure from Twitter API
            if obj.get("__typename") == "Tweet":
                # Get the legacy data which contains the actual tweet info
                tweet_result = obj.get("tweet_results", {}).get("result", {})
                legacy_data = tweet_result.get("legacy", {})

                # Get user info
                user_result = (
                    tweet_result.get("core", {})
                    .get("user_results", {})
                    .get("result", {})
                )
                user_legacy = user_result.get("legacy", {})

                # Filter out retweets by checking if it has a retweeted_status
                if "retweeted_status" not in legacy_data:
                    tweet_info = {
                        "author": user_legacy.get("screen_name", "")
                        or user_legacy.get("name", ""),
                        "text": legacy_data.get("full_text", "")
                        or legacy_data.get("text", ""),
                        "date": legacy_data.get("created_at", ""),
                        "likes": legacy_data.get("favorite_count", 0),
                        "url": f"https://twitter.com/{user_legacy.get('screen_name', '')}/status/{legacy_data.get('id_str', '')}",
                    }
                    tweets_list.append(tweet_info)

            # Also check for objects that might contain tweet data directly
            elif (
                "__typename" in obj
                and "itemContent" in obj
                and obj["__typename"] == "TimelineTweet"
            ):
                item_content = obj.get("itemContent", {})
                if item_content.get("__typename") == "Tweet":
                    traverse(item_content)  # Recursively process the actual tweet

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
    print("Testing fetcher with mock data...")
    data = fetch_tweets()
    if data:
        parsed_tweets = parse_tweets(data)
        if parsed_tweets:
            print("First parsed tweet:")
            print(
                json.dumps(parsed_tweets[0], indent=2)
            )  # Print only the first parsed tweet
        else:
            print("No tweets found or parsed.")
    else:
        print("Failed to fetch data from API.")
