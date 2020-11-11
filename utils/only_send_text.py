from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib  # 发送邮件

# 获取邮箱授权码  打开QQ邮箱 设置
smtp_server = 'smtp.qq.com'  # 邮箱的服务器地址
PORT = '465'
smtp_sender = '2205411511@qq.com'  # 邮箱的发送者
smtp_senderpassword = 'nhudmfiuqfjxdjcg'
smtp_receiver = '775494352@qq.com,996505911@qq.com'  # 邮箱的接收者
smtp_cc = '1219357895qq.com'  # 抄送
smtp_subject = '自动化测试报告'  # 邮件主题
smtp_body = '曾铸的测试邮件'  # 邮件正文

# 邮件的消息体

msg = MIMEText(smtp_body, "html", "utf-8")  # 邮件信息对象
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['Cc'] = smtp_cc
msg['subject'] = smtp_subject


smtp = smtplib.SMTP()
smtp.connect(smtp_server)
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_sender, smtp_receiver.split(',') +smtp_cc.split(','),
              msg.as_string())
