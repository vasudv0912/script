import faster_than_requests as requests
import json
import smtplib
import time
from email.mime.text import MIMEText
last_publish_id = 6048
recipients = ", ".join(['jsmith503@gmail.com', 'singhakash414@gmail.com'])
print("Script started...")

while True:
    try:
        d = requests.get2dict(
            "https://www.binance.com/gateway-api/v3/public/market/notice/get?page=1&rows=1")
        new_publish_id = json.loads(d[3]['data'])[0]['id']
        if new_publish_id > last_publish_id:
            last_publish_id = new_publish_id
            new_title = json.loads(d[3]['data'])[0]['title']
            print(new_title, last_publish_id)
            msg = MIMEText("Title:- "+str(new_title)+" // Publish Time:- " +
                           str(json.loads(d[3]['data'])[0]['time'])+"// Current Time:-" + str(time.time()*1000))
            msg['Subject'] = "Binance Update: " + str(new_title)
            msg['From'] = 'vasudv0912@gmail.com'
            msg['To'] = recipients
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("vasudv0912@gmail.com", "vasu9@0906")
            server.sendmail('vasudv0912@gmail.com',
                            recipients, msg.as_string())
            server.quit()
        time.sleep(0.05)
    except Exception as e:
        print(str(e)+" will try after 4 sec // " + str(time.time()*1000))
        time.sleep(4)
