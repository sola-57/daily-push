#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
每日英语阅读理解推送 - GitHub Actions版本 (修复版)
修复了KeyError问题，使用.get()方法安全访问字典键
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
                    'options': ['A. Making money', 'B. Maintaining good health', 'C. Getting a promotion', 'D. Becoming famous'],
                    'answer': 'B',
                    'explanation': '文中第一段第一句明确指出"Regular exercise is essential for maintaining good health."'
                },
                {
                    'question': 'What does the author suggest for people who find it difficult to start exercising?',
                    'options': ['A. Join a gym immediately', 'B. Hire a personal trainer', 'C. Begin with small, manageable steps', 'D. Exercise for at least one hour daily'],
                    'answer': 'C',
                    'explanation': '文中第二段提到"The key is to begin with small, manageable steps."'
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

The future of education likely involves a blended approach, combining the best of digital innovation with proven traditional teaching methods. This hybrid model can personalize learning while maintaining the essential human elements of education.''',
            'questions': [
                {
                    'question': 'According to the passage, how has technology affected education?',
                    'options': ['A. It has made learning more difficult', 'B. It has made learning more accessible and engaging', 'C. It has eliminated the need for teachers', 'D. It has reduced student motivation'],
                    'answer': 'B',
                    'explanation': '文中第一段提到"Digital devices and online resources have made learning more accessible and engaging."'
                },
                {
                    'question': 'What challenge does technology in education present?',
                    'options': ['A. Students learn too quickly', 'B. Screen time concerns and digital divide', 'C. Teachers refuse to use technology', 'D. Schools have too much funding'],
                    'answer': 'B',
                    'explanation': '文中第二段提到屏幕时间问题和数字鸿沟（digital divide）。'
                },
                {
                    'question': 'What is the role of teachers in technology integration?',
                    'options': ['A. To replace technology with traditional methods', 'B. To select appropriate tools and ensure technology enhances learning', 'C. To avoid using any digital tools', 'D. To reduce human interaction in classrooms'],
                    'answer': 'B',
                    'explanation': '文中第三段指出教师必须选择合适的数字工具，并确保技术增强而不是取代有意义的人际互动。'
                },
                {
                    'question': 'What does the author predict about the future of education?',
                    'options': ['A. Complete replacement of teachers by technology', 'B. A blended approach combining digital and traditional methods', 'C. Elimination of all digital devices', 'D. Only online learning will exist'],
                    'answer': 'B',
                    'explanation': '文中最后一段提到"The future of education likely involves a blended approach, combining the best of digital innovation with proven traditional teaching methods."'
                }
            ]
        },
        {
            'title': 'The Importance of Sleep',
            'content': '''Sleep is a fundamental biological need that affects every aspect of our health and well-being. Despite its importance, many people do not get enough sleep due to busy schedules, stress, or poor sleep habits. Adults typically need 7-9 hours of sleep per night to function optimally.

During sleep, the body performs essential maintenance tasks. The brain consolidates memories and processes information from the day. The immune system strengthens its defenses against illness. Hormones that regulate appetite, growth, and stress are balanced during sleep.

Chronic sleep deprivation can have serious consequences. It impairs cognitive function, affecting memory, concentration, and decision-making abilities. It also increases the risk of accidents, weakens the immune system, and contributes to mental health problems such as anxiety and depression.

Improving sleep quality involves creating a consistent sleep schedule, maintaining a comfortable sleep environment, and avoiding stimulants like caffeine before bedtime. Small changes in sleep habits can lead to significant improvements in overall health and daily functioning.''',
            'questions': [
                {
                    'question': 'According to the passage, how many hours of sleep do adults typically need?',
                    'options': ['A. 4-5 hours', 'B. 5-6 hours', 'C. 7-9 hours', 'D. 10-12 hours'],
                    'answer': 'C',
                    'explanation': '文中第一段明确指出"Adults typically need 7-9 hours of sleep per night to function optimally."'
                },
                {
                    'question': 'What does the brain do during sleep?',
                    'options': ['A. Stops working completely', 'B. Consolidates memories and processes information', 'C. Only controls breathing', 'D. Produces caffeine'],
                    'answer': 'B',
                    'explanation': '文中第二段提到"The brain consolidates memories and processes information from the day."'
                },
                {
                    'question': 'What is a consequence of chronic sleep deprivation?',
                    'options': ['A. Improved memory', 'B. Better immune function', 'C. Impaired cognitive function', 'D. Increased energy'],
                    'answer': 'C',
                    'explanation': '文中第三段提到"It impairs cognitive function, affecting memory, concentration, and decision-making abilities."'
                },
                {
                    'question': 'What can improve sleep quality?',
                    'options': ['A. Drinking coffee before bed', 'B. Irregular sleep schedule', 'C. Creating a consistent sleep schedule and comfortable environment', 'D. Using electronic devices in bed'],
                    'answer': 'C',
                    'explanation': '文中最后一段提到改善睡眠质量的方法包括建立一致的睡眠时间表和保持舒适的睡眠环境。'
                }
            ]
        },
        {
            'title': 'Climate Change and Its Effects',
            'content': '''Climate change is one of the most pressing challenges facing the world today. The Earth\'s average temperature has risen significantly over the past century, primarily due to human activities such as burning fossil fuels and deforestation. This global warming trend is causing widespread environmental changes.

The effects of climate change are visible across the globe. Rising sea levels threaten coastal communities and island nations. Extreme weather events, including hurricanes, droughts, and heat waves, are becoming more frequent and severe. Ecosystems are being disrupted, leading to species extinction and loss of biodiversity.

Agriculture is particularly vulnerable to climate change. Changes in temperature and precipitation patterns affect crop yields and food security. Some regions may become too hot or dry to support traditional farming, while others may experience increased flooding.

Addressing climate change requires both mitigation and adaptation strategies. Reducing greenhouse gas emissions through renewable energy and sustainable practices is essential. At the same time, communities must adapt to changes that are already occurring, such as building flood defenses and developing drought-resistant crops.''',
            'questions': [
                {
                    'question': 'What is the main cause of global warming according to the passage?',
                    'options': ['A. Natural climate cycles', 'B. Solar radiation', 'C. Human activities like burning fossil fuels', 'D. Ocean currents'],
                    'answer': 'C',
                    'explanation': '文中第一段提到"primarily due to human activities such as burning fossil fuels and deforestation."'
                },
                {
                    'question': 'What effect of climate change is mentioned in the passage?',
                    'options': ['A. Decreased sea levels', 'B. Fewer extreme weather events', 'C. Rising sea levels and extreme weather', 'D. Improved air quality'],
                    'answer': 'C',
                    'explanation': '文中第二段提到海平面上升和极端天气事件变得更加频繁和严重。'
                },
                {
                    'question': 'Why is agriculture vulnerable to climate change?',
                    'options': ['A. Because farmers refuse to adapt', 'B. Because changes in temperature and precipitation affect crop yields', 'C. Because there is too much food production', 'D. Because climate change improves farming conditions'],
                    'answer': 'B',
                    'explanation': '文中第三段指出"Changes in temperature and precipitation patterns affect crop yields and food security."'
                },
                {
                    'question': 'What strategies are needed to address climate change?',
                    'options': ['A. Only mitigation strategies', 'B. Only adaptation strategies', 'C. Both mitigation and adaptation strategies', 'D. No action is needed'],
                    'answer': 'C',
                    'explanation': '文中最后一段明确指出"Addressing climate change requires both mitigation and adaptation strategies."'
                }
            ]
        },
        {
            'title': 'The Role of Reading in Modern Life',
            'content': '''Reading remains a vital skill in the digital age, despite the proliferation of video and audio content. Regular reading strengthens brain connections, improves vocabulary and comprehension skills, and enhances empathy by exposing readers to different perspectives and experiences.

Many people claim they do not have time to read, but this is often a matter of priorities rather than actual time constraints. Replacing just 30 minutes of television or social media with reading each day can result in completing 20 or more books per year. E-books and audiobooks make reading more accessible than ever.

Different types of reading serve different purposes. Fiction develops imagination and emotional intelligence. Non-fiction provides knowledge and practical skills. News and current events keep readers informed about the world. Professional reading supports career development.

The format of reading has evolved with technology, but the fundamental benefits remain unchanged. Whether reading physical books, e-readers, or smartphones, the cognitive and emotional benefits of engaging with written content continue to make reading a valuable activity in modern life.''',
            'questions': [
                {
                    'question': 'According to the passage, what is one benefit of regular reading?',
                    'options': ['A. It weakens brain connections', 'B. It reduces vocabulary', 'C. It strengthens brain connections and improves vocabulary', 'D. It decreases empathy'],
                    'answer': 'C',
                    'explanation': '文中第一段提到"Regular reading strengthens brain connections, improves vocabulary and comprehension skills."'
                },
                {
                    'question': 'What does the author say about people who claim they have no time to read?',
                    'options': ['A. They are correct', 'B. It is a matter of priorities rather than actual time constraints', 'C. They should quit their jobs', 'D. They need to sleep less'],
                    'answer': 'B',
                    'explanation': '文中第二段指出"this is often a matter of priorities rather than actual time constraints."'
                },
                {
                    'question': 'What does fiction reading develop according to the passage?',
                    'options': ['A. Only practical skills', 'B. Imagination and emotional intelligence', 'C. Professional career skills', 'D. News and current events knowledge'],
                    'answer': 'B',
                    'explanation': '文中第三段提到"Fiction develops imagination and emotional intelligence."'
                },
                {
                    'question': 'What does the author conclude about reading in modern life?',
                    'options': ['A. Reading is no longer valuable', 'B. Only physical books are beneficial', 'C. The fundamental benefits of reading remain unchanged despite format changes', 'D. People should stop reading'],
                    'answer': 'C',
                    'explanation': '文中最后一段指出"The format of reading has evolved with technology, but the fundamental benefits remain unchanged."'
                }
            ]
        }
    ]

    # 随机选择一篇文章
    reading = random.choice(reading_materials)
    return reading

def generate_email_content(reading):
    """
    生成邮件内容
    """
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>每日英语阅读理解</title>
        <style>
            body {{ font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .container {{ background: white; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); overflow: hidden; }}
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

    # 添加题目 - 使用.get()方法安全访问字典键，避免KeyError
    for i, q in enumerate(reading['questions'], 1):
        # 安全获取题目数据，使用默认值防止KeyError
        question_text = q.get('question', f'Question {i}')
        options = q.get('options', ['A.', 'B.', 'C.', 'D.'])
        answer = q.get('answer', 'A')
        explanation = q.get('explanation', '暂无解析')
      
        # 确保options列表至少有4个元素
        while len(options) < 4:
            options.append(f'{chr(65+len(options))}.')
      
        html += f"""
                <div class="question">
                    <div class="question-number">Question {i}:</div>
                    <p>{question_text}</p>
                    <div class="options">
                        <div class="option">{options[0]}</div>
                        <div class="option">{options[1]}</div>
                        <div class="option">{options[2]}</div>
                        <div class="option">{options[3]}</div>
                    </div>
                    <div class="answer">
                        <div class="answer-label">✅ 正确答案: {answer}</div>
                        <p><strong>解析:</strong> {explanation}</p>
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
    
        # 添加HTML内容
        msg.attach(MIMEText(content, 'html', 'utf-8'))
    
        # 连接SMTP服务器并发送
        server = smtplib.SMTP_SSL(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['smtp_port'])
        server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
        server.send_message(msg)
        server.quit()
    
        print("✅ 邮件发送成功！")
        return True
    
    except Exception as e:
        print(f"❌ 邮件发送失败: {str(e)}")
        return False

def main():
    """
    主函数
    """
    print("=" * 50)
    print("每日英语阅读理解推送")
    print("=" * 50)

    # 获取阅读材料
    reading = get_english_reading()
    print(f"已选择文章: {reading['title']}")

    # 生成邮件内容
    email_content = generate_email_content(reading)

    # 发送邮件
    subject = f"📚 每日英语阅读理解 - {datetime.now().strftime('%Y年%m月%d日')}"
    success = send_email(subject, email_content)

    if success:
        print("\n✅ 推送完成！")
    else:
        print("\n❌ 推送失败！")

    return success

if __name__ == "__main__":
    main()
