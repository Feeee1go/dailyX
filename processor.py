import os
import logging
import requests
import uuid
from datetime import datetime
from typing import List, Dict, Tuple
import re
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source="auto", target="zh-CN")


def download_image(url: str, save_dir: str) -> str:
    """
    Download image from URL and save to local directory
    """
    try:
        # Ensure the save directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Download the image
        response = requests.get(url)
        response.raise_for_status()

        # Generate a unique filename
        ext = ".jpg"  # Default extension
        if url.lower().endswith((".png", ".gif", ".jpeg", ".jpg")):
            ext = url[url.rfind(".") :]

        filename = f"img_{str(uuid.uuid4())}{ext}"
        filepath = os.path.join(save_dir, filename)

        # Save the image
        with open(filepath, "wb") as f:
            f.write(response.content)

        return filepath
    except Exception as e:
        logging.error(f"Failed to download image {url}: {str(e)}")
        return ""


def generate_markdown(tweets: List[Dict], obsidian_dir: str) -> Tuple[str, List[str]]:
    """
    Convert tweets list to formatted markdown content and download images
    Returns: (markdown_content, list_of_local_image_paths)
    """
    # Generate header with date
    current_date = datetime.now().strftime("%Y-%m-%d")
    md_content = f"# Daily Pulse - {current_date}\n\n"

    local_images = []  # Track downloaded images

    for idx, tweet in enumerate(tweets):
        author = tweet.get("author", "Unknown")
        text = tweet.get("text", "")
        date = tweet.get("date", "")
        likes = tweet.get("likes", 0)
        url = tweet.get("url", "")
        images = tweet.get("images", [])

        # Translate text
        translated_text = text
        try:
            translated_text = translator.translate(text)
        except Exception as e:
            logging.warning(
                f"Translation failed for tweet: {str(e)}, keeping original text"
            )
            translated_text = text  # Fallback to original text

        # Add section for each tweet
        md_content += f"### [{author}]({url})\n\n"
        md_content += f"**发布时间:** {date} | ❤️ {likes}\n\n"
        md_content += f"> {text}\n\n"
        md_content += f"> 🇨🇳 译文：{translated_text}\n\n"

        # Add images if any (between translation and link), download them and update path
        for img_url in images:
            local_path = download_image(img_url, os.path.join(obsidian_dir, "images"))
            if local_path:
                local_images.append(local_path)
                # Use relative path in markdown
                rel_path = os.path.relpath(local_path, obsidian_dir)
                md_content += f"![Image]({rel_path})\n\n"

        md_content += "[🔗 查看原帖]({})\n\n".format(url)

        # Add separator except for the last tweet
        if idx < len(tweets) - 1:
            md_content += "---\n\n"

    return md_content, local_images


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
