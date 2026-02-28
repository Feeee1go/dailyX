import logging
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

    # Generate markdown content
    logging.info("Generating markdown content...")
    md_content = generate_markdown(tweets)

    # Save to Obsidian
    logging.info("Saving to Obsidian...")
    save_to_obsidian(md_content)

    # Send email
    logging.info("Sending email...")
    send_email(md_content)

    logging.info("Daily Pulse automation completed successfully!")


if __name__ == "__main__":
    main()
