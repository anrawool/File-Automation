import __meta
from datetime import datetime
import imaplib
import email
from PvtInfo.info import Google_Token, Email_Address
from Controllers.data import NexusEmailObject
import html2text
import pytz
import os


class Gmail_Connection():
    def __init__(self, criteria='ALL', part='inbox', gmail_address=None, gmail_password=None, download_attachments = True, attachment_path='./') -> None:
        self.gmail_connection = imaplib.IMAP4_SSL("imap.gmail.com")
        self.download_attachments = download_attachments
        self.attachment_path = attachment_path
        self.part = part
        self.criteria = criteria
        if gmail_address != None and gmail_password != None:
            self.gmail_connection.login(gmail_address, gmail_password)
        elif gmail_password == None and gmail_password == None:
            self.gmail_connection.login(Email_Address, Google_Token)
        else:
            raise ValueError("Gmail address and gmail password, both are required")

    def select_part(self):
        self.gmail_connection.select(self.part)
    
    def search_messages(self):
        self.status, self.messages = self.gmail_connection.search(None, self.criteria)
        self.messages = self.messages[0].split(b' ')

    # TODO: Add this function with integration in the date,py itself with exception cases too
    def convert_date(self, date_time_string):
        parsed_date_time = datetime.strptime(date_time_string, "%a, %d %b %Y %H:%M:%S %z")
        ist_timezone = pytz.timezone('Asia/Kolkata')
        ist_date_time = parsed_date_time.astimezone(ist_timezone)
        formatted_date_time = ist_date_time.strftime("%A, %d %B %Y %I:%M:%S %p")
        return formatted_date_time


    def filter_messages(self):
        self.final_results = []
        for mail in self.messages:
            res, msg = self.gmail_connection.fetch(mail, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    # parse a bytes email into a message object
                    msg = email.message_from_bytes(response[1])
                    # extract email details
                    subject = msg["subject"]
                    from_ = msg["from"]
                    date_str = self.convert_date(msg['Date'])
                    body = ''


                    for part in msg.walk():
                        # extract content type of email
                        content_type = part.get_content_type()
                        content_disposition = str(part.get("Content-Disposition"))

                        if content_type == "text/plain":
                            body = part.get_payload(decode=True).decode()
                        elif content_type == "text/html":
                            html = part.get_payload(decode=True).decode()
                            body = html2text.html2text(html)
                        elif "attachment" in content_disposition and self.download_attachments:
                            self.has_attachment = True
                            # download attachment and save it
                            filename = part.get_filename()
                            if filename:
                                folder_name = self.attachment_path + "attachments"
                                if not os.path.isdir(folder_name):
                                    os.mkdir(folder_name)
                                filepath = os.path.join(folder_name, filename)
                                open(filepath, "wb").write(part.get_payload(decode=True))
                        else:
                            self.has_attachment = False

                        if body.strip():
                            email_object = NexusEmailObject(sender_address=from_, receiver_address=Email_Address, date=date_str, subject=subject, body=body, has_attachment=self.has_attachment)
                            # Assuming NexusEmailObject.body contains the email content

                            # Split the email body into lines
                            email_lines = body.split('\n')

                            cleaned_body = ''

                            # Set a flag to indicate when to start capturing the main content
                            capture_main_content = False

                            # Iterate through the lines of the email body
                            for line in email_lines:
                                # Ignore lines that start with ">"
                                if not line.startswith('>'):
                                    # Start capturing the main content when a non-quoted line is encountered
                                    capture_main_content = True
                                if capture_main_content:
                                    # Append the line to the cleaned body
                                    cleaned_body += line + '\n'

                            # Remove leading and trailing whitespace
                            cleaned_body = cleaned_body.strip()

                            # Print the cleaned email body
                            print(cleaned_body)

                            print('\n')
                            self.final_results.append(email_object)
            return self.final_results
    def close_connection(self):
        self.gmail_connection.close()
        self.gmail_connection.logout()

    def collect_emails(self):
        self.select_part()
        self.search_messages()
        final_messages = self.filter_messages()
        return final_messages


# email_connection = Gmail_Connection(criteria='FROM "someone@something.something"')
# messages = email_connection.collect_emails()