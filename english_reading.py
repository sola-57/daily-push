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
        msg['From'] = Header(f"英语阅读 <{EMAIL_CONFIG['sender']}>", 'utf-8')
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
    subject = f"📚 每日英语阅读 - {datetime.now().strftime('%m月%d日')}"
    content = f"""
    <html>
    <body style="font-family: Arial; max-width: 600px; margin: 0 auto;">
        <h2>📚 每日英语阅读</h2>
        <p>{datetime.now().strftime('%Y年%m月%d日')}</p>
        <hr>
        <h3>阅读文章</h3>
        <p><strong>The Importance of Lifelong Learning</strong></p>
        <p>In today's rapidly changing world, the concept of education has evolved significantly. 
        Lifelong learning has become essential for personal and professional growth. 
        Whether through formal education, online courses, or self-study, 
        continuous learning helps individuals stay competitive and adapt to new challenges.</p>
        <hr>
        <h3>阅读理解题</h3>
        <p><strong>1. What is the main idea of the passage?</strong></p>
        <p>A) Education is only important for young people<br>
        B) Lifelong learning is essential in modern society<br>
        C) Online courses are the best way to learn<br>
        D) Formal education is no longer necessary</p>
      
        <p><strong>答案: B</strong></p>
        <p><strong>解析:</strong> 文章主要讲述了终身学习在现代社会的重要性。</p>
        <hr>
        <p style="color: #999; font-size: 12px;">GitHub Actions自动发送</p>
    </body>
    </html>
    """
  
    if send_email(subject, content):
        print("✅ 英语阅读推送完成！")
    else:
        print("❌ 英语阅读推送失败！")

if __name__ == "__main__":
    main()
