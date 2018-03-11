import smtplib
from email.header import Header
from email.mime.text import MIMEText

class ArchiveRecordService:
    def snedEmail(self):
        msg = MIMEText('hello,send by python...', 'plain', 'utf-8')

        msg['From'] = Header('python爱好者', 'utf-8')
        msg['To'] = Header('管理员', 'utf-8')
        msg['Subject'] = Header('来自SMTP的问候', 'utf-8')

        server = smtplib.SMTP("smtp.qq.com", 25)  # SMTP协议默认端口是25
        server.set_debuglevel(1)
        server.starttls()
        server.login("344501823@qq.com", "slregekgovoocaeg") #登录QQ邮箱，注意
        server.sendmail("344501823@qq.com", ["344501823@qq.com"], msg.as_string())
        server.quit()
