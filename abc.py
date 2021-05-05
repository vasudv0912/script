import faster_than_requests as requests
import json
import smtplib
import time
from email.mime.text import MIMEText
currenttitle0=""
recipients= ", ".join(['jsmith503@gmail.com','singhakash414@gmail.com'])
print("Script started...")

while True:
	try: 
		d = requests.get2dict("https://www.binance.com/gateway-api/v3/public/market/notice/get?page=1&rows=1")
		currenttitle1=(json.loads(d[3]['data'])[0]['title'])
		publishtimestramp=(json.loads(d[3]['data'])[0]['time'])
		if currenttitle0!=currenttitle1:
			currenttitle0=currenttitle1
			print(currenttitle0)
			msg = MIMEText("Title:- "+str(currenttitle0)+" // Publish Time:- "+str(publishtimestramp)+"// Current Time:-"+ str(time.time()*1000))
			msg['Subject'] = "Binance Update: " + str(currenttitle0)
			msg['From'] = 'vasudv0912@gmail.com'
			msg['To'] = recipients
			server=smtplib.SMTP_SSL("smtp.gmail.com" , 465)
			server.login("vasudv0912@gmail.com","vasu9@0609")
			server.sendmail('vasudv0912@gmail.com',recipients, msg.as_string())
			server.quit()
	except Exception as e: 
		print(str(e)+" will try after 3 sec")
		time.sleep(3)