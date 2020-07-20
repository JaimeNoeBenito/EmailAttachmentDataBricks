from os.path import basename
from email.mime.application import MIMEApplication
from email import encoders
from email.mime.base import MIMEBase

def sendMailAttachment(Subject, fromaddr, toaddr, path, file, body_text):
	"""Send emails with attachments from databricks

	  :Subjet: subject of the email
	  :fromaddr: sender of the email 
	  :toaddr: (list of) receivers
	  :path: temporary path (DataLake) to store the file that will be attached in the eail
	  :file: filename
	  :body_text: body of the email
	  """
    msg = MIMEMultipart()
      
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = Subject
    BodyMail = msg.as_string()
    
    mail_file = MIMEBase('application', 'csv')
    mail_file.set_payload(open(path + file, 'rb').read())
    mail_file.add_header('Content-Disposition', 'attachment', filename=file)
    encoders.encode_base64(mail_file)
    msg.attach(mail_file)
    msg.attach(MIMEText(body_text))
    
    server = smtplib.SMTP(SMTPServer, 25)
    server.login(SMTPUser, SMTPPwd)
    server.sendmail(fromaddr, toaddr, msg.as_string())