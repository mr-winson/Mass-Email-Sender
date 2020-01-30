# Do not edit the next two lines
import pandas as pd
import smtplib

# edit the next two lines to fit your gmail
SenderAddress = "googleUsername@gmail.com"
password = "password"

# dont edit the next four lines
e = pd.read_excel("emails.xlsx")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Edit the next line
server.login("googleUsername@gmail.com", "password")

# this is the body of the email, edit it "\n" is a line break -- https://docs.python.org/2.0/ref/strings.html -- for more \ commands
msg = "message of the email"

# this is the subject of the email, edit it
subject = "Subject of the email"

# dont edit anything below this line
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail(SenderAddress, email, body)
server.quit()
