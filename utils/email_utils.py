#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:mail_utils.py
# @time:2020/5/10 10:41 上午
import smtplib, os
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from utils.read_conf import read_conf
from utils.Zip_file import zip_dir


class EmailUtils:
    def __init__(self, smtp_file_path=None):
        self.smtp_server = read_conf.get_conf_smtp_server
        self.smtp_sender = read_conf.get_conf_smtp_sender
        self.smtp_senderpassword = 'nhudmfiuqfjxdjcg'
        self.smtp_receiver = read_conf.get_conf_smtp_receiver
        self.smtp_cc = read_conf.get_conf_smtp_cc
        self.smtp_subject = read_conf.get_conf_smtp_subject
        self.smtp_body = read_conf.get_conf_smtp_body
        self.smtp_file = smtp_file_path

    def mail_content(self):
        if self.smtp_file is not None:
            if self.smtp_file.split('.')[-1].__eq__('zip'):
                return self.__mail_zip_content()
            else:
                return self.__mail_content_by_zip()

        else:
            return self.__mail_text_content()

    def __mail_content_by_zip(self):
        report_zip_path = self.smtp_file + '.zip'
        zip_dir(self.smtp_file, report_zip_path)
        print('压缩')
        self.smtp_file = report_zip_path
        print(self.smtp_file)
        msg = self.mail_content()
        return msg

    def __mail_text_content(self):
        msg = MIMEText(self.smtp_body, "html", "utf-8")  # 邮件信息对象
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def __mail_zip_content(self):
        msg = MIMEMultipart()
        with open(self.smtp_file, 'rb') as f:
            mine = MIMEBase('zip', 'zip', filename=self.smtp_file.split('/')[-1])
            mine.add_header('Content-Disposition', 'attachment',
                            filename=('gb2312', '', self.smtp_file.split('/')[-1]))
            mine.add_header('Content-ID', '<0>')
            mine.add_header('X-Attachment-Id', '0')
            mine.set_payload(f.read())
            encoders.encode_base64(mine)
            msg.attach(mine)
        msg.attach(MIMEText(self.smtp_body, "html", "utf-8"))
        msg['from'] = self.smtp_sender
        msg['to'] = self.smtp_receiver
        msg['Cc'] = self.smtp_cc
        msg['subject'] = self.smtp_subject
        return msg

    def semnd_email(self, msg):
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtp_server)  # 465
        except Exception as e:
            print('连接服务器失败')
            smtp = smtplib.SMTP_SSL()
            # smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        # msg = self.mail_content()
        try:
            smtp.login(user=self.smtp_sender, password=self.smtp_senderpassword)
        except Exception as e:
            print('登录失败，失败原因：%s' % e)
        try:
            smtp.sendmail(self.smtp_sender, self.smtp_receiver.split(',') + self.smtp_cc.split(','), msg.as_string())
        except Exception as e:
            print('邮件发送失败，失败原因：%s' % e)
        # except Exception as e:
        #     print('发送失败,失败原因:%s' % e)
        smtp.quit()


if __name__ == '__main__':
    smtp_file_path = os.path.join(os.path.dirname(__file__), '../reports/report_20201111_143526接口自动化标题V1.0')
    emils = EmailUtils(smtp_file_path)
    msg = emils.mail_content()
    emils.semnd_email(msg)
