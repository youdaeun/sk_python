import smtplib
from email.mime.text import MIMEText

send_email = "youremail"
send_pwd="yourpassword"
recv_email = "youremail"

smtp_name = "smtp.naver.com"
smtp_port = 587

text = "text입니다."

msg = MIMEText(text, 'plain', 'utf-8') 
msg['Subject'] = "메일 제목 입력"  
msg['From'] = send_email          
msg['To'] = recv_email            

email_string = msg.as_string()
print(email_string)

s = smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, email_string)
s.quit()