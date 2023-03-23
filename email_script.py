import smtplib, ssl
import csv

from email.mime.text import MIMEText
from smtplib import SMTP

smtp_server = "smtp.mail.umich.edu"
port = 587  # For starttls
sender_email = "EMAIL HERE" # Your email here
password = "PASSWORD HERE" # Password here

# Variables for message
firstname = ""
lastname = ""
receiver_email = ""
midterm = "0"
lettergrade = "0"
overallgrade = "0"
hwavg = 0.0

# Column indices for accesing the csv file
firstname_idx = 0
lastname_idx = 1
email_idx = 3
midterm_idx = 11
lettergrade_idx = 12
overallgrade_idx = 13
hwavg_idx = 15

# Create a secure SSL context
context = ssl.create_default_context()

# Try to log in to server and send email
server = smtplib.SMTP(smtp_server,port)

with open("./grades.csv", 'r') as file:
    csvreader = csv.reader(file)
    num = 0
    for row in csvreader:
        if (num != 0):
            firstname = row[firstname_idx]
            lastname = row[lastname_idx]
            receiver_email = row[email_idx]
            midterm = row[midterm_idx]
            lettergrade = row[lettergrade_idx]
            overallgrade = row[overallgrade_idx]
            avg = row[hwavg_idx]
            hwavg = round(((float(avg)/.40) * 100),2)
            message = ""
            with open('email_script.txt', 'r') as msg:
                message = msg.read().format(
                    firstname=firstname,
                    lastname=lastname,
                    receiver_email=receiver_email,
                    midterm=midterm,
                    lettergrade=lettergrade,
                    overallgrade=overallgrade,
                    hwavg=hwavg,
                )
            try:
                msg = MIMEText(message)
                msg['Subject'] = 'EECS376W23 Grade Update'
                msg['From'] = 'dchoo@umich.edu'
                msg['To'] = receiver_email
                print("Sending to...", receiver_email)
                # ========= Email sending procedure =========================
                # Uncomment these lines to unleash the script!
                # server.starttls(context=context) # Secure the connection
                # server.login(sender_email, password)
                # server.sendmail(sender_email, receiver_email, msg.as_string())
                # ============================================================
                
                print(message)
                print("Done!")
            except Exception as e:
                # Print any error messages to stdout
                print(e)
        num += 1


