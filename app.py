import imaplib
import email
from bs4 import BeautifulSoup
import requests
import telebot
import os

# Email credentials
EMAIL_USERNAME = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

# Telegram Bot token and chat ID
TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
CHAT_ID = os.environ.get('CHAT_ID')

FILTER_FROM = os.environ.get('FILTER_FROM')
FILTER_TO = os.environ.get('FILTER_TO')
FILTER_SUBJECT_1 = os.environ.get('FILTER_SUBJECT_1')
FILTER_SUBJECT_2 = os.environ.get('FILTER_SUBJECT_2')
FILTER_HREF_1 = os.environ.get('FILTER_HREF_1')
FILTER_HREF_2 = os.environ.get('FILTER_HREF_2')
BOT_MESSAGE = os.environ.get('BOT_MESSAGE')

# Establish connection to the email mailbox
mail = imaplib.IMAP4_SSL(os.environ.get('IMAP_HOST'), 993)
mail.login(EMAIL_USERNAME, EMAIL_PASSWORD)
mail.select('INBOX')

# Search for unread emails
status, data = mail.search(None, 'UNSEEN')
email_ids = data[0].split() if data[0] else []
email_ids = email_ids[-10:]  # Select the last 10 unread emails

if not email_ids:  # Check if the list is empty
    print("No new unseen emails found.")
    mail.logout()  # Disconnect from the mailbox
    exit()  # End the program

for email_id in email_ids:
    status, data = mail.fetch(email_id, '(BODY[])')
    raw_email = data[0][1]
    email_message = email.message_from_bytes(raw_email)

    # Check the filter criteria for the email
    if (email_message['from'] == FILTER_FROM and email_message['to'] == FILTER_TO and
            (email_message['subject'] == FILTER_SUBJECT_1 or email_message['subject'] == FILTER_SUBJECT_2)):

        for part in email_message.walk():
            if part.get_content_type() == 'text/html':
                html_content = part.get_payload(decode=True).decode()

                # Extract links from the HTML content
                soup = BeautifulSoup(html_content, 'html.parser')
                links = [a['href'] for a in soup.find_all('a', href=True)]
                for link in links:
                    if FILTER_HREF_1 in link or FILTER_HREF_2 in link:
                        print(link)

                        # Initialize Telegram Bot and send message
                        bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)
                        bot.send_message(CHAT_ID, BOT_MESSAGE + link)

mail.logout()
