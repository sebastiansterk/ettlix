# ettlix
ettlix is an **E**mail **T**o **T**elegram **L**ink **E**xtractor.


## Features

- Connects to an email account using IMAP protocol to retrieve unread emails. Currently only icloud/me.com email tested and supported.
- Filters emails based on sender, recipient, and subject criteria.
- Extracts links from HTML content in the email body.
- Sends the extracted links to a Telegram chat using a Telegram bot.

## Configuration
You can modify the `run.sh` according to your needs.
|Environment variable|Description|Example value|
|---|---|---|
|`EMAIL_USER`|Your email account username|john.doe@example.com|
|`EMAIL_PASSWORD`|Your email account password|P@ssw0rd123|
|`IMAP_HOST`|IMAP server hostname|imap.example.com|
|`TELEGRAM_BOT_TOKEN`|Telegram Bot token|1234567890:abcdefg|
|`CHAT_ID`|Telegram chat ID where messages will be sent|-1234567890|
|`FILTER_FROM`|Sender email address to filter|sender@example.com|
|`FILTER_TO`|Recipient email address to filter|recipient@example.com|
|`FILTER_SUBJECT_1`|First subject keyword to filter|Important|
|`FILTER_SUBJECT_2`|Second subject keyword to filter|Newsletter|
|`FILTER_HREF_1`|First link keyword to filter|verify|
|`FILTER_HREF_2`|Second link keyword to filter|update-primary-location|
|`BOT_MESSAGE`|Message to send along with the extracted link|🤖 Here is the link to something: |

## How filtering works
1. Only the last 10 unseen emails are processed.
2. Emails are processed if they meet the following criteria:
  - The email is from the specified sender (FROM).
  - The email is addressed to the specified recipient (TO).
  - The email's subject matches either SUBJECT_1 or SUBJECT_2.
3. Only links that meet the following criteria will be sent to the Telegram chat:
  - The link contains either HREF_1 or HREF_2.

## Run it
```
bash ./run.sh
```
You can create a cronjob to execute ettlix every X minutes.
