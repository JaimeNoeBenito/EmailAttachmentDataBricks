# Import smtplib library to send email in python.
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Define the source and target email address.
strFrom = "your_server_or_source_email@your_domain.com"
strTo = "your_destinaton_email_jaime@your_domain.com"
# Create an instance of MIMEMultipart object, pass 'related' as the constructor parameter.
msgRoot = MIMEMultipart('related')
# Set the email subject.
msgRoot['Subject'] = 'This email contain both Html, text and one image.'
# Set the email from email address.
msgRoot['From'] = strFrom
# Set the email to email address.
msgRoot['To'] = strTo
# Set the multipart email preamble attribute value. Please refer https://docs.python.org/3/library/email.message.html to learn more.
msgRoot.preamble = '====================================================='
# Create a 'alternative' MIMEMultipart object. We will use this object to save plain text format content.
msgAlternative = MIMEMultipart('alternative')
# Attach the bove object to the root email message.
msgRoot.attach(msgAlternative)
# Create a MIMEText object, this object contains the plain text content.
msgText = MIMEText('This object contains the plain text content of this email.')
# Attach the MIMEText object to the msgAlternative object.
msgAlternative.attach(msgText)
# Create a MIMEText object to contains the email Html content. There is also an image in the Html content. The image cid is image1.
msgText = MIMEText('<b>This is the <i>HTML</i> content of this email</b> and it contains an image.<br><img src="cid:image1"><br>', 'html')
# Attach the above html content MIMEText object to the msgAlternative object.
msgAlternative.attach(msgText)
# Open a file object to read the image file, the image file is located in the file path it provide.
#fp = open('/usr/var/test.jpg', 'rb')
fp = open('/dbfs/you_datalake_path_here/figure.png', 'rb')
# Create a MIMEImage object with the above file object.
msgImage = MIMEImage(fp.read())
# Do not forget close the file object after using it.
fp.close()
# Add 'Content-ID' header value to the above MIMEImage object to make it refer to the image source (src="cid:image1") in the Html content.
msgImage.add_header('Content-ID', '<image1>')
# Attach the MIMEImage object to the email body.
msgRoot.attach(msgImage)
# Create an smtplib.SMTP object to send the email.
smtp = smtplib.SMTP(SMTPServer, <your_port_number_here>) #like -->  smtplib.SMTP(SMTPServer, 123)
# Connect to the SMTP server.
# smtp.connect('smtp.code-learner.com')
# Login to the SMTP server with username and password.
smtp.login(SMTPUser, SMTPPwd)



# Send email with the smtp object sendmail method.
smtp.sendmail(strFrom, strTo, msgRoot.as_string())
# Quit the SMTP server after sending the email.
smtp.quit()