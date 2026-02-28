import logging
import os
from fetcher import fetch_tweets
from processor import generate_markdown, save_to_obsidian
from notifier import send_email


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Fetch tweets
    logging.info("Fetching tweets...")
    tweets = fetch_tweets()

    if not tweets:
        logging.warning("No tweets found or fetched")
        return

    # Generate markdown content and download images
    logging.info("Generating markdown content and downloading images...")
    obsidian_dir = os.getenv("OBSIDIAN_DIR")
    if not obsidian_dir:
        logging.error("OBSIDIAN_DIR environment variable not set")
        return

    md_content, local_images = generate_markdown(tweets, obsidian_dir)

    # Save to Obsidian
    logging.info("Saving to Obsidian...")
    save_to_obsidian(md_content)

    # Send email with embedded images
    logging.info("Sending email with embedded images...")
    send_email(md_content, local_images)

    logging.info("Daily Pulse automation completed successfully!")


if __name__ == "__main__":
    main()
