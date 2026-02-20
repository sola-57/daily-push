import smtplib
import random
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

EMAIL_CONFIG = {
    'sender': '2773343617@qq.com',
    'password': os.environ.get('EMAIL_PASSWORD', ''),
    'receiver': '2773343617@qq.com',
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465
}

def send_email(subject, content):
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = Header(f"股市资讯 <{EMAIL_CONFIG['sender']}>", 'utf-8')
        msg['To'] = Header(EMAIL_CONFIG['receiver'], 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg.attach(MIMEText(content, 'html', 'utf-8'))
      
        server = smtplib.SMTP_SSL(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
        server.sendmail(EMAIL_CONFIG['sender'], [EMAIL_CONFIG['receiver']], msg.as_string())
        server.quit()
        print(f"✅ 邮件发送成功: {subject}")
        return True
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

def main():
    subject = f"📊 每日股市资讯 - {datetime.now().strftime('%m月%d日')}"
    content = f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 0 auto;">
        <h2>📊 每日股市资讯</h2>
        <p>{datetime.now().strftime('%Y年%m月%d日')}</p>
        <hr>
        <h3>1. A股三大指数集体收涨</h3>
        <p>今日A股三大指数集体收涨，科技股表现强势。</p>
        <h3>2. 美联储暗示可能暂停加息</h3>
        <p>美联储最新会议纪要显示可能很快适合暂停加息。</p>
        <h3>3. 新能源汽车销量超预期</h3>
        <p>新能源汽车销量同比增长35%，超出市场预期。</p>
        <hr>
        <p style="color: #999; font-size: 12px;">GitHub Actions自动发送</p>
    </body>
    </html>
    """
  
    if send_email(subject, content):
        print("✅ 股市资讯推送完成！")
    else:
        print("❌ 股市资讯推送失败！")

if __name__ == "__main__":
    main()
