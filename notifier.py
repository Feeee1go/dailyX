import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime


def send_email(md_content: str):
    """
    Send email with markdown content
    """
    smtp_server = os.getenv("SMTP_SERVER") or ""
    smtp_port_str = os.getenv("SMTP_PORT") or ""
    sender_email = os.getenv("SENDER_EMAIL") or ""
    sender_password = os.getenv("SENDER_PASSWORD") or ""
    receiver_email = os.getenv("RECEIVER_EMAIL") or ""

    if not all(
        [smtp_server, smtp_port_str, sender_email, sender_password, receiver_email]
    ):
        logging.error("Missing email configuration in environment variables")
        return

    try:
        smtp_port = int(smtp_port_str)
    except (ValueError, TypeError):
        logging.error("Invalid SMTP port value")
        return

    try:
        # Create message
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = receiver_email
        current_date = datetime.now().strftime("%Y-%m-%d")
        msg["Subject"] = f"[Daily Pulse] X 热门资讯 - {current_date}"

        # Attach content
        msg.attach(MIMEText(md_content, "plain"))

        # Connect to server and send email
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")
