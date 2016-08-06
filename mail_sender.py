import smtplib

USER_NAME =  
PASSWORD = 

SUBJECT = raw_input("Enter the subject :")

CONTENT = raw_input("Enter the mail content :")

FROM = 

TO = 

def mail_sender(username, password, message):
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.login(username, password)
	server.sendmail(FROM, TO, message)
	server.close()


mail_sender(USER_NAME, PASSWORD, CONTENT)
