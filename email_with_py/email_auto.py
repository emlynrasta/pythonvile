import email
import smtplib
import ssl
from email.message import EmailMessage
import imaplib
import config


class Emailer:
    def __init__(self):
        self.email = config.senders_email
        self.from_email = f"Rasta at work <{self.email}>"
        self.password = config.sender_auth
        self.context = ssl.create_default_context()
        print('context set')
        self.server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context)
        self.mail = imaplib.IMAP4_SSL('imap.gmail.com')

    def send_mail(self, receivers, subject, body):
        self.server.login(self.email, self.password)  # login to send emails
        print('you have logged in')
        # make sure receivers is a list
        assert isinstance(receivers, list)
        # instantiate Email_message
        email = EmailMessage()
        email['From'] = self.from_email
        email['To'] = receivers
        email['Subject'] = subject
        email.set_content(body)
        # email.add_attachment()

        print('lets send this shit')
        not_sent = True
        while not_sent:
            try:
                with self.server as server:
                    server.sendmail(self.email, receivers, email.as_string())
                    print('email has been sent')
                    not_sent = False
            except Exception as err:
                print('failed to send email \n', err)

    def check_inbox(self):
        self.mail.login(self.email, self.password)  # login to check inbox
        print('you have logged in')
        self.mail.select("inbox", readonly=False)  # select inbox to read from
        # search for unseen mail
        _, search_data = self.mail.search(None, 'UNSEEN')
        # print(search_data)

        # print out the inbox
        for num in search_data[0].split():
            # print(num)
            # dictionary to store mail data
            email_data = {}
            # mail list
            my_messages = []
            # fetch data for each of the mails
            _, data = self.mail.fetch(num, '(RFC822)')
            # print(data[0])
            _, b = data[0]
            email_message = email.message_from_bytes(b)
            # print(email_message)
            for header in ['Subject', 'To', 'From', 'date']:
                # print("{}: {}".format(header, email_message[header]))
                email_data[header] = email_message[header]
            # further parsing
            for part in email_message.walk():
                if part.get_content_type() == "text/plain":
                    # prints the text of the mail_msg
                    body = part.get_payload(decode=True)
                    email_data['body'] = body.decode()
                    # print(body.decode())
                elif part.get_content_type() == "text/html":
                    html_body = part.get_payload(decode=True)
                    email_data['html_body'] = html_body.decode()
            my_messages.append(email_data)
            return my_messages


if __name__ == '__main__':
    cow = Emailer()
    my_clients = ['emlynat02@gmail.com', 'emlynb99@gmail.com', 'emlynatochon@yahoo.com']
    msg_subject = 'email_to you'
    msg_body = """do you need jesus"""
    cow.send_mail(my_clients, msg_subject, msg_body)
    # my_inbox = cow.check_inbox()
    # print(my_inbox)
