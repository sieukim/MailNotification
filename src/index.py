import dotenv
import os
import schedule
import time
import smtplib
from email.message import EmailMessage
from api.scan_items import scan_items
from api.delete_item import delete_item
from api.tracking import tracking

dotenv.load_dotenv(dotenv.find_dotenv())

# 알림 메일 전송
def send_mail(id, user):
    SMPT_SERVER = 'smtp.gmail.com'
    SMTP_PORT = 465
    smpt = smtplib.SMTP_SSL(SMPT_SERVER, SMTP_PORT)
    email, password = os.environ['email'], os.environ['password']
    smpt.login(email, password)
    message = EmailMessage()
    message.set_content(f'우편 조회 바로가기 -> https://service.epost.go.kr/trace.RetrieveDomRigiTraceList.comm?sid1={id}')
    message['Subject'] = '우편 발송이 시작되었어요.'
    message['From'] = email
    message['To'] = user
    smpt.send_message(message)
    smpt.quit()

# 전체 우표 번호 조회 
def tracking_all():
    for item in scan_items():
        id, user = item['id'], item['user']
        success = tracking(id)
        if success:
            send_mail(id, user)
            delete_item(id)

schedule.every(1).day.at("19:00").do(tracking_all)
while True:
    schedule.run_pending()
    time.sleep(60)