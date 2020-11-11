from email import encoders
from email.mime.multipart import MIMEMultipart  # 带附件
from email.mime.text import MIMEText  # 只要是发送不带附件的类
import smtplib, os  # 发送邮件
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# dir_path = os.path.join(os.path.dirname(__file__), '..', 'report/禅道自动化测试报告V1.2/禅道自动化测试报告V1.2.zip')
# 获取邮箱授权码  打开QQ邮箱 设置

smtp_server = 'smtp.qq.com'  # 邮箱的服务器地址
smtp_sender = '2205411511@qq.com'  # 邮箱的发送者
smtp_senderpassword = 'nhudmfiuqfjxdjcg'  # 授权码
smtp_receiver = '775494352@qq.com,996505911@qq.com'  # 邮箱的接收者
smtp_cc = '1219357895qq.com'  # 抄送
smtp_zhuti_title = '自动化测试报告'  # 邮件主题
smtp_body = '曾铸的测试邮件'  # 邮件正文
smtp_file = os.path.join(os.path.dirname(__file__), '../reports/report_20201111_103810.html接口测试报告V1.0.zip')  # 先手工压缩在测试文档
# smtp_file = 'D:\\PycharmProjects\\Git_PO_Zentao\\report\\禅道自动化测试报告V1.2\\禅道自动化测试报告V1.2.zip'
# 配置附件

msg = MIMEMultipart()
with open(smtp_file, 'rb') as f:
    mine = MIMEBase('zip', 'zip', filename=smtp_file.split('/')[-1])
    mine.add_header('Content-Disposition', 'attachment', filename=('gb2312', '', smtp_file.split('/')[-1]))
    mine.add_header('Content-ID', '<0>')
    mine.add_header('X-Attachment-Id', '0')
    mine.set_payload(f.read())
    encoders.encode_base64(mine)
    msg.attach(mine)

# 邮件的消息体
# 邮件正文
msg.attach(MIMEText(smtp_body, 'html', 'utf-8'))  # 添加邮件正文
msg['from'] = smtp_sender
msg['to'] = smtp_receiver
msg['cc'] = smtp_cc
msg['subject'] = smtp_zhuti_title

smtp = smtplib.SMTP()
smtp.connect(smtp_server)  # 465
smtp.login(user=smtp_sender, password=smtp_senderpassword)
smtp.sendmail(smtp_sender, smtp_receiver.split(',') + smtp_cc.split(','), msg.as_string())
