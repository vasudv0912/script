import faster_than_requests as requests
import datetime
import json
import smtplib
import time
from email.mime.text import MIMEText
server=smtplib.SMTP_SSL("smtp.gmail.com" , 465)
server.login("vasudv0912@gmail.com","vasu9@0609")
currenttitle0=""
count=0
print("Script started...")
while True:
	try: 
		x=datetime.datetime.now()
		d = requests.get2dict("https://www.binance.com/gateway-api/v3/public/market/notice/get?page=1&rows=1")
		count+=1
		print(count)
		currenttitle1=(json.loads(d[3]['data'])[0]['title'])
		publishtimestramp=(json.loads(d[3]['data'])[0]['time'])
		if currenttitle0!=currenttitle1:
			currenttitle0=currenttitle1
			msg = MIMEText("Title:- "+str(currenttitle0)+" // Publish Time:- "+str(publishtimestramp)+"// Current Time:-"+str(datetime.datetime.now()))
			msg['Subject'] = "Binance Update: " 
			msg['From'] = 'vasudv0912@gmail.com'
			recipients= ['jsmith503@gmail.com','singhakash414@gmail.com']
			msg['To'] = ", ".join(recipients)
			server.sendmail('vasudv0912@gmail.com',recipients, msg.as_string())
	except Exception as e: 
		print(str(e)+" will try after 3 sec")
		time.sleep(3)  
		continue