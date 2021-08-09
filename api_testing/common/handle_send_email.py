import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from api_testing.common.handle_path import REPORT_DIR


def send_report(report_name):
    """通过邮箱发送测试报告给指定的用户"""
    # 第1步：连接qq smtp服务器，模拟登陆
    # 1.1连接到qq  smtp服务器 —— smtp.qq.com
    smtp = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
    # lhereksoonbebedc 是开启smtp的时候，qq给的授权码
    smtp.login(user='756093055@qq.com', password='lhereksoonbebedc')
    # 第2步：构建一封邮件
    msg = MIMEMultipart()
    msg['Subject'] = report_name[-4]  # 邮件标题
    msg['To'] = '756093055@qq.com'
    msg['From'] = '756093055@qq.com'
    # 构建发送内容
    text = MIMEText('您好，附件是测试报告，请查收！', _charset='utf8')
    msg.attach(text)  # 把邮件内容添加到邮件中
    #上传附件
       #读取附件内容，bytes格式
    report_file= os.path.join(REPORT_DIR,report_name)
    with open(report_file,mode='rb')as f:
        content=f.read()
        report=MIMEApplication(content) #构造附件对象
        report.add_header('content-disposition','attchment',filename=report_name)
        msg.attach(report)#把构造的附件添加到邮件中
    # 第3步：发送邮件
    smtp.send_message(msg, from_addr='756093055@qq.com', to_addrs='756093055@qq.com')


if __name__ == '__main__':
    send_report('0809测试报告')
