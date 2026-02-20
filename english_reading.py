#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日英语阅读理解推送 - GitHub Actions版本
"""

import smtplib
import random
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

# 邮件配置
EMAIL_CONFIG = {
    'sender': os.environ.get('EMAIL_SENDER', '2773343617@qq.com'),
    'password': os.environ.get('EMAIL_PASSWORD', ''),
    'receiver': os.environ.get('RECEIVER_EMAIL', '2773343617@qq.com'),
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465
}

def get_english_reading():
    """获取英语阅读理解内容"""
    # 同等学力英语难度文章
    reading_materials = [
        {
            'title': 'The Benefits of Regular Exercise',
            'content': '''Regular exercise is essential for maintaining good health. It not only helps control weight but also reduces the risk of heart disease, diabetes, and certain types of cancer. Physical activity can improve mental health by reducing stress, anxiety, and depression.

Many people find it difficult to start an exercise routine. The key is to begin with small, manageable steps. Walking for just 30 minutes a day can make a significant difference. As fitness improves, activities can be gradually increased in intensity and duration.

Exercise also has social benefits. Joining a sports team or fitness class can help people make new friends and stay motivated. Group activities provide accountability and make exercise more enjoyable.

The most important thing is to find activities that are enjoyable. Whether it is swimming, cycling, dancing, or playing basketball, choosing something fun makes it easier to stick with the routine. Consistency is more important than intensity when it comes to long-term health benefits.''',
            'questions': [
                {
                    'question': 'According to the passage, what is the main benefit of regular exercise?',
                    'options': ['A. Making money', 'B. Maintaining good health', 'C. Finding a job', 'D. Traveling abroad'],
                    'answer': 'B',
                    'explanation': '文中第一段明确提到"Regular exercise is essential for maintaining good health."'
                },
                {
                    'question': 'What does the author suggest for people who find it difficult to start exercising?',
                    'options': ['A. Run a marathon immediately', 'B. Join an expensive gym', 'C. Begin with small, manageable steps', 'D. Hire a personal trainer'],
                    'answer': 'C',
                    'explanation': '文中第二段指出"The key is to begin with small, manageable steps."'
                },
                {
                    'question': 'What social benefit does exercise provide according to the passage?',
                    'options': ['A. Getting a promotion', 'B. Making new friends', 'C. Winning competitions', 'D. Becoming famous'],
                    'answer': 'B',
                    'explanation': '文中第三段提到"Joining a sports team or fitness class can help people make new friends."'
                },
                {
                    'question': 'What is the most important factor for long-term health benefits?',
                    'options': ['A. Exercise intensity', 'B. Exercise duration', 'C. Consistency', 'D. Exercise type'],
                    'answer': 'C',
                    'explanation': '文中最后一句指出"Consistency is more important than intensity when it comes to long-term health benefits."'
                }
            ]
        },
        {
            'title': 'The Impact of Technology on Education',
            'content': '''Technology has transformed education in remarkable ways. Digital devices and online resources have made learning more accessible and engaging for students of all ages. Interactive software and educational apps allow learners to practice skills at their own pace.

However, technology in education also presents challenges. Screen time concerns have led educators to balance digital learning with traditional methods. Additionally, not all students have equal access to devices and reliable internet connections, creating a digital divide.

Teachers play a crucial role in integrating technology effectively. They must select appropriate digital tools and ensure that technology enhances rather than replaces meaningful human interaction. Professional development helps educators stay current with rapidly evolving educational technologies.

The future of education likely involves a blended approach, combining the best of digital innovation with proven traditional teaching methods. This hybrid model can personalize learning while maintaining the social aspects of education that are vital for student development.''',
            'questions': [
                {
                    'question': 'What is one benefit of technology in education mentioned in the passage?',
                    'options': ['A. Reducing teacher salaries', 'B. Making learning more accessible', 'C. Eliminating homework', 'D. Shortening school hours'],
                    'answer': 'B',
                    'explanation': '文中第一段提到"Digital devices and online resources have made learning more accessible and engaging."'
                },
                {
                    'question': 'What challenge does technology in education present?',
                    'options': ['A. Too many textbooks', 'B. The digital divide', 'C. Longer school days', 'D. More homework'],
                    'Answer': 'B',
                    'explanation': '文中第二段指出"not all students have equal access to devices and reliable internet connections, creating a digital divide."'
                },
                {
                    'question': 'What is the teacher\'s role in integrating technology?',
                    'options': ['A. Replacing all traditional methods', 'B. Selecting appropriate digital tools', 'C. Avoiding technology completely', 'D. Buying new devices'],
                    'answer': 'B',
                    'explanation': '文中第三段提到"They must select appropriate digital tools and ensure that technology enhances rather than replaces meaningful human interaction."'
                },
                {
                    'question': 'What does the author predict about the future of education?',
                    'options': ['A. Complete elimination of technology', 'B. A blended approach combining digital and traditional methods', 'C. All learning will be online', 'D. Teachers will be replaced by robots'],
                    'answer': 'B',
                    'explanation': '文中最后一段指出"The future of education likely involves a blended approach, combining the best of digital innovation with proven traditional teaching methods."'
                }
            ]
        },
        {
            'title': 'The Importance of Sleep',
            'content': '''Sleep is a fundamental biological need that affects every aspect of human health. During sleep, the body repairs tissues, consolidates memories, and regulates hormones. Adults typically need 7-9 hours of sleep per night for optimal functioning.

Chronic sleep deprivation can have serious consequences. It impairs cognitive function, reduces immune system effectiveness, and increases the risk of accidents. Long-term sleep deficiency has been linked to obesity, cardiovascular disease, and mental health disorders.

Many factors can disrupt sleep patterns. Stress, electronic device use before bedtime, irregular schedules, and caffeine consumption are common culprits. Creating a sleep-friendly environment and establishing consistent bedtime routines can significantly improve sleep quality.

Some people believe they can function well on minimal sleep, but research consistently shows that most adults need adequate sleep to perform at their best. Prioritizing sleep is an investment in overall health and productivity.''',
            'questions': [
                {
                    'question': 'According to the passage, what happens during sleep?',
                    'options': ['A. The body becomes completely inactive', 'B. The body repairs tissues and consolidates memories', 'C. The brain stops working', 'D. Nothing important happens'],
                    'answer': 'B',
                    'explanation': '文中第一段提到"During sleep, the body repairs tissues, consolidates memories, and regulates hormones."'
                },
                {
                    'question': 'What is a consequence of chronic sleep deprivation?',
                    'options': ['A. Improved memory', 'B. Better immune function', 'C. Impaired cognitive function', 'D. Increased energy'],
                    'answer': 'C',
                    'explanation': '文中第二段指出"It impairs cognitive function, reduces immune system effectiveness, and increases the risk of accidents."'
                },
                {
                    'question': 'What can disrupt sleep patterns according to the passage?',
                    'options': ['A. Reading books', 'B. Regular exercise', 'C. Electronic device use before bedtime', 'D. Drinking water'],
                    'answer': 'C',
                    'explanation': '文中第三段提到"Stress, electronic device use before bedtime, irregular schedules, and caffeine consumption are common culprits."'
                },
                {
                    'question': 'What does research show about people who claim to function well on minimal sleep?',
                    'options': ['A. They are correct', 'B. Most adults need adequate sleep to perform at their best', 'C. They are healthier than others', 'D. They do not need sleep at all'],
                    'answer': 'B',
                    'explanation': '文中最后一段指出"research consistently shows that most adults need adequate sleep to perform at their best."'
                }
            ]
        }
    ]
  
    # 随机选择一篇文章
    return random.choice(reading_materials)

def generate_email_content(reading):
    """生成邮件HTML内容"""
    html = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; }}
            .container {{ max-width: 800px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; margin-bottom: 30px; }}
            .header h1 {{ margin: 0; font-size: 28px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; }}
            .section {{ background: #f8f9fa; padding: 20px; margin-bottom: 20px; border-radius: 8px; border-left: 4px solid #667eea; }}
            .section h2 {{ color: #667eea; margin-top: 0; }}
            .article {{ background: white; padding: 20px; border-radius: 8px; margin-bottom: 20px; border: 1px solid #e0e0e0; }}
            .article h3 {{ color: #333; border-bottom: 2px solid #667eea; padding-bottom: 10px; }}
            .article p {{ text-align: justify; }}
            .question {{ background: #f0f4ff; padding: 15px; margin: 15px 0; border-radius: 8px; }}
            .question-number {{ font-weight: bold; color: #667eea; }}
            .options {{ margin: 10px 0; }}
            .option {{ margin: 5px 0; padding: 8px; background: white; border-radius: 4px; }}
            .answer {{ background: #d4edda; padding: 15px; margin-top: 10px; border-radius: 8px; border-left: 4px solid #28a745; }}
            .answer-label {{ font-weight: bold; color: #28a745; }}
            .footer {{ text-align: center; margin-top: 40px; padding: 20px; color: #666; font-size: 14px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📚 每日英语阅读理解</h1>
                <p>同等学力英语考试难度 | {datetime.now().strftime('%Y年%m月%d日')}</p>
            </div>
          
            <div class="section">
                <h2>📝 阅读文章</h2>
                <div class="article">
                    <h3>{reading['title']}</h3>
                    <p>{reading['content'].replace(chr(10), '<br>')}</p>
                </div>
            </div>
          
            <div class="section">
                <h2>❓ 阅读理解题目</h2>
    """
  
    # 添加题目
    for i, q in enumerate(reading['questions'], 1):
        html += f"""
                <div class="question">
                    <div class="question-number">Question {i}:</div>
                    <p>{q['question']}</p>
                    <div class="options">
                        <div class="option">{q['options'][0]}</div>
                        <div class="option">{q['options'][1]}</div>
                        <div class="option">{q['options'][2]}</div>
                        <div class="option">{q['options'][3]}</div>
                    </div>
                    <div class="answer">
                        <div class="answer-label">✅ 正确答案: {q['answer']}</div>
                        <p><strong>解析:</strong> {q['explanation']}</p>
                    </div>
                </div>
        """
  
    html += """
            </div>
          
            <div class="footer">
                <p>💡 提示: 建议先阅读文章，尝试自己回答问题，然后再查看答案解析</p>
                <p>📧 每日推送 | 坚持学习，每天进步一点点</p>
            </div>
        </div>
    </body>
    </html>
    """
  
    return html

def send_email(subject, content):
    """
    发送邮件
    """
    try:
        print(f"正在发送邮件到: {EMAIL_CONFIG['receiver']}")
      
        msg = MIMEMultipart()
        # 修复From头部格式
        msg['From'] = f"Daily Push <{EMAIL_CONFIG['sender']}>"
        msg['To'] = EMAIL_CONFIG['receiver']
        msg['Subject'] = Header(subject, 'utf-8')
      
        msg.attach(MIMEText(content, 'html', 'utf-8'))
      
        server = smtplib.SMTP_SSL(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
        server.sendmail(EMAIL_CONFIG['sender'], [EMAIL_CONFIG['receiver']], msg.as_string())
        server.quit()
      
        print(f"✅ 邮件发送成功！")
        return True
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

def main():
    """主函数"""
    print("=" * 70)
    print("📚 每日英语阅读理解推送")
    print("=" * 70)
  
    # 获取阅读材料
    reading = get_english_reading()
    print(f"📖 已选择文章: {reading['title']}")
  
    # 生成邮件内容
    email_content = generate_email_content(reading)
  
    # 发送邮件
    subject = f"📚 每日英语阅读理解 - {datetime.now().strftime('%Y年%m月%d日')}"
    success = send_email(subject, email_content)
  
    if success:
        print("\n" + "=" * 70)
        print("✅ 每日英语阅读理解推送完成！")
        print("=" * 70)
    else:
        print("\n" + "=" * 70)
        print("❌ 推送失败")
        print("=" * 70)

if __name__ == "__main__":
    main()
