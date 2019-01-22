# coding=utf-8
# 
# send email
# 

from os.path import join
import smtplib
from email.mime.text import MIMEText
import logging
logger = logging.getLogger(__name__)



def sendMail(msgText, subject, sender, recipients, mailServer, timeout):
	"""
	Send email to recipients.
	[String] msgText
	[String] subject
	[String] sender (the address that appears in 'from' field)
	[String] recipients (a string containing comma separated addresses)
	[String] mailServer (mail server address)
	[Float] timeout (time out for mail server)
	"""
	msg = MIMEText(msgText)
	msg['Subject'] = subject
	msg['From'] = sender
	msg['To'] = recipients

	smtp = smtplib.SMTP(mailServer, timeout=timeout)
	smtp.send_message(msg)
	smtp.quit()