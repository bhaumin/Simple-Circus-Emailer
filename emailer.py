import smtplib
import getpass
from settings import SMTP_SERVER, SMTP_PORT


def compose_message(from_email, to_email, name, forecast, schedule):
    message = str.format(("From: {0}\n"
                          "To: {1}\n"
                          "Subject: Welcome to the Circus!\n"
                          "Hi {2}!\n\n"
                          "{3}\n\n"
                          "{4}\n\n"
                          "Hope to see you there!"),
                         from_email, to_email, name, forecast, schedule)
    return message


def send_emails(recipients, schedule, forecast):
    smtp_server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp_server.starttls()

    print(("You need to input your gmail.com address as the sender email below. "
           "But first, you need to temporarily allow non-secure apps "
           "under your GMail -> My Account -> Connected apps and Sites. "
           "Obviously, use one of your un-important dummy GMail accounts, "
           "NOT YOUR REAL ONE."))

    allowed_non_secure_apps = input("\nDid you ALLOW non-secure apps under your GMail account? (Y/N): ")

    if allowed_non_secure_apps is None or allowed_non_secure_apps.upper() != "Y":
        print("No worries!, Try again next time.")
        return

    sender = input("Sender email (you@gmail.com): ")
    password = getpass.getpass("Password (your gmail password): ")
    smtp_server.login(sender, password)

    count = 0

    for to_email, name in recipients.items():
        smtp_server.sendmail(sender,
                             to_email,
                             compose_message(sender, to_email, name, forecast, schedule))
        count += 1

    print("\nEmails sent to", count, "recipients!")
    smtp_server.quit()
