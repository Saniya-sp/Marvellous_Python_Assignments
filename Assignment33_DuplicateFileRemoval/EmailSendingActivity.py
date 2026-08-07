#####################################
# Mall Sending Activity using Python

#Program: Simple Gmail Mail Sender
#Author: Piyush Khairnar Marvellous Infosystems
#Purpose: Send mail using Python SMTP
######################################

import smtplib
from email.message import EmailMessage

#Function: Marvellous send_mail
#Description: Sends email using Gmail SMTP server

def send_mail(sender, app_password, receiver, subject, body, file_name):
    #Step 1: Create Email object
    msg = EmailMessage()
    #Step 2: Set mail headers
    msg["From"]=sender
    msg["To"] = receiver
    msg["Subject"] = subject
    #Step 3: Add mail body 
    msg.set_content(body)
    #Step 4: Create SMTP SSL connection manually 
    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)
    #Step 5: Login using Gmail + App password 
    smtp.login(sender, app_password)

    if file_name:
        # Attach file
        filename = file_name
        # filepath = r"D:\Reports\Report.pdf"
        with open(filename, "rb") as f:
            file_data = f.read()
            file_name = f.name

        msg.add_attachment(
            file_data,
            maintype="application",
            subtype="octet-stream",
            filename=file_name
        )

    #Step 6: Send the email 
    smtp.send_message(msg)
    #Step 7: Close connection manually
    smtp.quit()

#Function: main
# Description:Driver code
#
def main():
    #Always use separate temporary/testing account
    sender_email = "pathansaniyaxxxx@gmail.com"
    #App password generated from Google account
    app_password = "ztwuxxxxxxxxxxxxxxx"
    #Your second email for testing
    receiver_email = "saniyapathanxxxxx@gmail.com"
    subject = 'Test mail'
    body = 'Hi, this is you from your another mail id.'
    file_name = None
    send_mail(sender_email, app_password, receiver_email, subject, body, file_name)
    print("Mail sent successfully.")

if __name__ == "__main__":
    main()

    