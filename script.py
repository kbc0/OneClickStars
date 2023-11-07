#!/usr/bin/env python

import imaplib
import email
import re
import time
import quopri
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def extract_verification_code(body):
    # Decode the body if it's in quoted-printable encoding
    body = quopri.decodestring(body).decode("utf-8")

    # Adjust the regex to capture the verification code that might be followed by whitespace or '=' character
    match = re.search(
        r"Verification Code: (\d+)(?:\s|=)*for your Bilkent University Secure Login Gateway",
        body,
        re.DOTALL,  # re.DOTALL allows '.' to match any character including newline
    )
    if match:
        return match.group(
            1
        ).strip()  # strip() is used to remove any leading/trailing whitespace
    return None


# Function to check the inbox for verification code
def check_inbox(username, password, imap_server):
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(username, password)
    mail.select("inbox")

    status, data = mail.search(None, "UNSEEN")
    mail_ids = []

    for block in data:
        mail_ids += block.split()

    for i in mail_ids:
        status, data = mail.fetch(i, "(RFC822)")

        for response_part in data:
            if isinstance(response_part, tuple):
                message = email.message_from_bytes(response_part[1])

                mail_from = message["from"]
                mail_subject = message["subject"]
                print(mail_from)
                print(f"Email Subject: {mail_subject}")  # Debug print

                if "Secure Login Gateway E-Mail Verification Code" in mail_subject:
                    if message.is_multipart():
                        mail_content = ""

                        for part in message.get_payload():
                            if part.get_content_type() == "text/plain":
                                mail_content += part.get_payload()
                    else:
                        mail_content = message.get_payload()

                    print(f"Email Content: {mail_content}")  # Debug print

                    code = extract_verification_code(mail_content)
                    mail.logout()
                    return code
    mail.logout()
    return None


# This is your existing instant_stars function with additional steps for verification code handling
def instant_stars():
    driverSTARS = webdriver.Chrome()

    # Open STARS login page
    driverSTARS.get("https://stars.bilkent.edu.tr/srs/")

    # Fill in the username and password
    WebDriverWait(driverSTARS, 10).until(
        EC.presence_of_element_located((By.ID, "LoginForm_username"))
    )
    email_field = driverSTARS.find_element(By.ID, "LoginForm_username")
    #Fill the below field with your credentials
    email_field.send_keys("yourID")

    WebDriverWait(driverSTARS, 10).until(
        EC.presence_of_element_located((By.ID, "LoginForm_password"))
    )
    password_field = driverSTARS.find_element(By.ID, "LoginForm_password")
    #Fill the below field with your credentials
    password_field.send_keys("yourPassword")

    # Log in
    password_field.send_keys(Keys.RETURN)

    print("Waiting for verification code...")
    time.sleep(10)

    # Wait and check for the verification code in the email
    verification_code = check_inbox(
        #Fill the below field with your credentials
        "your.mail@ug.bilkent.edu.tr", "yourMailPassword", "mail.bilkent.edu.tr"
    )
    print(verification_code)
    # Enter the verification code in the webpage
    if verification_code:
        WebDriverWait(driverSTARS, 10).until(
            EC.presence_of_element_located((By.ID, "EmailVerifyForm_verifyCode"))
        )
        verification_input = driverSTARS.find_element(
            By.ID, "EmailVerifyForm_verifyCode"
        )
        verification_input.send_keys(verification_code)

        WebDriverWait(driverSTARS, 10).until(
            EC.element_to_be_clickable((By.NAME, "yt0"))
        )
        verify_button = driverSTARS.find_element(By.NAME, "yt0")
        verify_button.click()
    else:
        print(
            "No verification code received. Please check your email manually.",
        )

    time.sleep(3000)

    if driverSTARS is not None:
        driverSTARS.quit()


if __name__ == "__main__":
    instant_stars()
