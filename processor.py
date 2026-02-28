import os
import logging
from datetime import datetime
from typing import List, Dict


def generate_markdown(tweets: List[Dict]) -> str:
    """
    Convert tweets list to formatted markdown content
    """
    # Generate header with date
    current_date = datetime.now().strftime("%Y-%m-%d")
    md_content = f"# Daily Pulse - {current_date}\n\n"

    for idx, tweet in enumerate(tweets):
        author = tweet.get("author", "Unknown")
        text = tweet.get("text", "")
        date = tweet.get("date", "")
        likes = tweet.get("likes", 0)
        url = tweet.get("url", "")

        # Add section for each tweet
        md_content += f"### [{author}]({url})\n\n"
        md_content += f"**发布时间:** {date} | ❤️ {likes}\n\n"
        md_content += f"> {text}\n\n"
        md_content += "[🔗 查看原帖]({})\n\n".format(url)

        # Add separator except for the last tweet
        if idx < len(tweets) - 1:
            md_content += "---\n\n"

    return md_content


def save_to_obsidian(md_content: str):
    """
    Save markdown content to obsidian vault
    """
    obsidian_dir = os.getenv("OBSIDIAN_DIR")
    if not obsidian_dir:
        logging.error("OBSIDIAN_DIR environment variable not set")
        return

    # Generate filename with current date
    current_date = datetime.now().strftime("%Y-%m-%d")
    filename = f"{current_date}-Daily-Pulse.md"
    filepath = os.path.join(obsidian_dir, filename)

    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # Write content to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(md_content)

        logging.info(f"Successfully saved to Obsidian: {filepath}")
    except Exception as e:
        logging.error(f"Failed to save to Obsidian: {str(e)}")
