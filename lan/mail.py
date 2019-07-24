import smtplib
from email.mime.text import MIMEText


class Mail(object):
    def __init__(self, host="", port=465, user="", passwd=""):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.port = port

    def send(self, receivers="", subject="", content=""):
        msg = MIMEText(content, 'html', 'utf-8')
        msg['Subject'] = subject
        msg['From'] = self.user
        msg['To'] = receivers
        try:
            s = smtplib.SMTP_SSL(self.host, self.port)
            s.login(self.user, self.passwd)
            s.sendmail(self.user, receivers, msg.as_string())
            print('发送成功')
        except:
            print('发送失败')


if __name__ == '__main__':
    m = Mail("smtp.qq.com", 465, "13629582436@qq.com", "optaspqzopfycfjd")
    m.send("643826784@qq.com", "你好", "哈哈")
