from imap_tools import MailBox, AND
from connector import EmailConnector

EMAIL = "pandu22ds@gmail.com"
PASSWORD = "kukx mvlc gkqr nhqs"

connector = EmailConnector()

with MailBox("imap.gmail.com").login(
    EMAIL,
    PASSWORD,
    "INBOX"
) as mailbox:

    for msg in mailbox.fetch(AND(seen=False)):

        payload = {
            "subject": msg.subject,
            "sender": msg.from_,
            "date": str(msg.date),
            "body": msg.text
}

        result = connector.send(payload)

        print(result)