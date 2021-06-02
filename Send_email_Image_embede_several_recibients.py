import matplotlib.pyplot as plt
plt.scatter(x=[1,2,3], y=[2,4,3])
plt.savefig('/dbfs/patH_datalake/figure.png')

################################

def email_with_image(toaddr, Subject, body, path_image):

  import smtplib
  from email.mime.multipart import MIMEMultipart
  from email.mime.text import MIMEText
  from email.mime.image import MIMEImage

  # Define the source and target email address.
  strFrom = "your_server_adress@your_domain.com"

  # Create an instance of MIMEMultipart object, pass 'related' as the constructor parameter.
  msgRoot = MIMEMultipart('related')
  # Set the email subject.
  msgRoot['Subject'] = Subject
  # Set the email from email address.
  msgRoot['From'] = strFrom
  # Set the email to email address.
  msgRoot['To'] = ", ".join(toaddr)
#   msgRoot['To'] = ", ".join(toaddr)
#   strTo = ", ".join(toaddr)
  # Set the multipart email preamble attribute value. Please refer https://docs.python.org/3/library/email.message.html to learn more.
  msgRoot.preamble = '====================================================='
  # Create a 'alternative' MIMEMultipart object. We will use this object to save plain text format content.
  msgAlternative = MIMEMultipart('alternative')
  # Attach the bove object to the root email message.
  msgRoot.attach(msgAlternative)
  # Create a MIMEText object, this object contains the plain text content.
  #msgText = MIMEText('Aqui va vuestro texto plano chicos - de nada.')
  msgText = MIMEText(body)
  # Attach the MIMEText object to the msgAlternative object.
  msgAlternative.attach(msgText)
  # Create a MIMEText object to contains the email Html content. There is also an image in the Html content. The image cid is image1.
  msgText = MIMEText('<b>Aqui va vuestro texto plano chicos <i>HTML</i> - de nada. </b> contiene una imagen guardada en nuestro datalake .<br><img src="cid:image1"><br><b> Pruba 2 </b>', 'html')
  # Attach the above html content MIMEText object to the msgAlternative object.
  msgAlternative.attach(msgText)
  # Open a file object to read the image file, the image file is located in the file path it provide.
  #fp = open('/usr/var/test.jpg', 'rb')
  fp = open(path_image, 'rb')
  # Create a MIMEImage object with the above file object.
  msgImage = MIMEImage(fp.read())
  # Do not forget close the file object after using it.
  fp.close()
  # Add 'Content-ID' header value to the above MIMEImage object to make it refer to the image source (src="cid:image1") in the Html content.
  msgImage.add_header('Content-ID', '<image1>')
  # Attach the MIMEImage object to the email body.
  msgRoot.attach(msgImage)
  # Create an smtplib.SMTP object to send the email.
  #smtp = smtplib.SMTP(SMTPServer, <your_port_number>)
  smtp = smtplib.SMTP(SMTPServer, 123)
  # Connect to the SMTP server.
  # smtp.connect('smtp.code-learner.com')
  # Login to the SMTP server with username and password.
  smtp.login(SMTPUser, SMTPPwd)

  
  # Send email with the smtp object sendmail method.
  smtp.sendmail(strFrom, toaddr, msgRoot.as_string())
#   smtp.sendmail(strFrom, strTo, msgRoot.as_string())

  # server.sendmail(fromaddr, toaddr, msg.as_string())
  # Quit the SMTP server after sending the email.
  smtp.quit()

################################

Subject = 'Problem solved: email con imagenes embebidas'
# toaddr = ["bladibladibladi@your_domain.com",  "user_2@your_domain.com"]
body = 'Aqui va  texto plano .'
path_image = '/dbfs/your_datalake_path/figure.png'
email_with_image(toaddr.split(','), Subject, body, path_image)

################################

