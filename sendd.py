import time
import c1
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def startt():
   try:
      msg = MIMEMultipart()
      msg['Subject'] = 'i run today sh'
      msg['From'] = ''
      msg['To'] = ''
      s = smtplib.SMTP('smtp.qq.com', 587)
      s.ehlo()
      s.starttls()
      s.ehlo()
      s.login('', '')
      s.sendmail('', '', msg.as_string())
      s.quit()
   except:
      print("Mail error")



   for x in xrange(8000):
      try:

       print x
       c1.catch()
       time.sleep(2)

      except:
        print("catch error")

if __name__ == '__main__':
    startt()

// email using qq email send
