import ssl
import smtplib
from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

class Mail:
    def __init__(self, port=587, user='gixam@jubaan.ai', password='ItsG00dT0BeH0me', smtp='smtp.office365.com'):
        self.port = port
        self.user = user
        self.smtp = smtp
        self.password = password

    def sendMail(self, subject: str = 'Gixam Test Session', to: str = '', message: str = ''):
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP(self.smtp, self.port)
            server.starttls(context=context)
            server.login(user=self.user, password=self.password)

            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.user
            msg['To'] = to

            msg.attach(MIMEText(message, 'plain'))
            server.sendmail(self.user, to, msg.as_string())
        except Exception as e:
            print(f"Exception: {e}")
        finally:
            server.quit()

    def sendHTMLMail(self, subject: str = 'Gixam Test Session', to: str = '', message: str = '', attachments=None):
        try:
            context = ssl.create_default_context()
            server = smtplib.SMTP(self.smtp, self.port)
            server.starttls(context=context)
            server.login(user=self.user, password=self.password)

            msgRoot = MIMEMultipart('related')
            msgRoot['From'] = 'Gixam Unit'
            msgRoot['To'] = to
            msgRoot['Subject'] = subject
            msg = MIMEMultipart('alternative')
            msgRoot.attach(msg)
            html_message = MIMEText(message, "html")
            msg.attach(html_message)

            if attachments:
                atch = 0
                for fa in attachments:
                    with open(fa, "rb") as attachment:
                        # Add file as application/octet-stream
                        # Email client can usually download this automatically as attachment
                        part = MIMEBase("application", "octet-stream")
                        part.set_payload(attachment.read())
                        # part=MIMEImage(attachment.read())

                    encoders.encode_base64(part)
                    atch += 1
                    # part.add_header('Content-Type', 'image/png')
                    part.add_header('Content-ID', f"<image{atch}>")
                    part.add_header('Content-Disposition',
                                    f'attachment; filename=image{atch}.png')

                    msgRoot.attach(part)

            server.sendmail(self.user, to, msgRoot.as_string())

        except Exception as e:
            print(f"Exception: {e}")
        finally:
            server.quit()


if __name__ == "__main__":
    mail = Mail()

    mail.sendMail("this is a test from the edc server", "amit@jubaan.com", f"this is the body of the test, hello {datetime.datetime.now()}")

