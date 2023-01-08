import csv
import smtplib
from email.message import EmailMessage
import requests

with open('Sample.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)

    for row in reader:
        message = row[0]
        email = row[1]
        phone_number = row[2]
        country = row[3]

        url = "https://api.sms-magic.com/v1/sms/send"
        payload = "mobile_number=9552772600&sms_text=helloWorld&sender_id=market"
        headers = {
            'apiKey': "9f81fddf27be1aa3e73a0619392cbc0c",
        }
        response = requests.request("GET", url, headers=headers, params=payload)
        print(response.text)
        msg = EmailMessage()
        msg.set_content(message)
        msg['Subject'] = 'Important message'
        msg['From'] = 'samrat7352@gmail.com'
        msg['To'] = email
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('samrat7352@gmail.com', 'YOUR_EMAIL_PASSWORD')
        
        server.send_message(msg)
        server.quit()
