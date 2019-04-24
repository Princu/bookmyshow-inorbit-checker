#Running script using urllib2
import sys
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import re
import smtplib
from email.mime.text import MIMEText

url = "https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190501" #<Movie's link where all theatres are present>
username = #<username>
password = #<password>
sender = #<sender's email>
receivers = [<List of recievers>]
message = MIMEText("""Head over here to check if the script worked correctly. :P
https://in.bookmyshow.com/buytickets/avengers-endgame-bengaluru/movie-bang-ET00100668-MT/20190501""")
message['Subject'] = "Yo!!. We are on, book tickets now, it's available now :D"
message['From'] = "GoGoMaster<GoGoMaster@GoGo.com>"
message['To'] = ", ".join(receivers)
#Yes, google has a open SMTP server :D
smtpObj = smtplib.SMTP('smtp.gmail.com:587')
while True:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(req).read()
        soup = BeautifulSoup(page,features="html.parser")
        for element in soup.findAll(attrs = {'class': re.compile(r"listing")}):
            ele = element.findAll(text = re.compile("PVR: VR Bengaluru, Whitefield Road"))
            if ele:
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.login(username, password)
                smtpObj.sendmail(sender, receivers, message.as_string())
                smtpObj.quit()
                print ("Successfully sent email")
                sys.exit()
                time.sleep(5)
