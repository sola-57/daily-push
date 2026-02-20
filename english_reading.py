# english_reading.py
import smtplib
import random
import os
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

# 邮件配置
EMAIL_CONFIG = {
    'sender': '2773343617@qq.com',
    'password': os.environ.get('EMAIL_PASSWORD', ''),
    'receiver': os.environ.get('RECEIVER_EMAIL', '2773343617@qq.com'),
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465
}

def get_reading_material():
    """获取英语阅读材料"""
    readings = [
        {
            'title': 'The Benefits of Reading',
            'content': """Reading is one of the most important skills a person can have. It opens up new worlds and allows us to learn about different cultures, ideas, and perspectives. Studies have shown that regular reading can improve memory, reduce stress, and even increase empathy.

In today's digital age, many people spend more time looking at screens than reading books. However, research suggests that reading physical books may be better for our eyes and sleep patterns than reading on electronic devices. The blue light emitted by phones and tablets can interfere with our natural sleep cycles.

Despite the rise of digital media, libraries remain important community resources. They provide free access to books, computers, and educational programs. Many libraries have also adapted to modern needs by offering e-books and online resources.

Reading is not just about entertainment or education. It is also a fundamental skill for success in the workplace. Employers consistently rank reading and writing as essential skills for employees. People who read regularly tend to have better vocabulary, communication skills, and critical thinking abilities.""",
            'questions': [
                {
                    'question': 'According to the passage, what is one benefit of regular reading?',
                    'options': ['A. It improves physical strength', 'B. It improves memory', 'C. It increases appetite', 'D. It reduces physical exercise'],
                    'answer': 'B',
                    'explanation': '文中明确提到"Studies have shown that regular reading can improve memory, reduce stress, and even increase empathy."'
                },
                {
                    'question': 'Why might reading physical books be better than reading on electronic devices?',
                    'options': ['A. Physical books are cheaper', 'B. Electronic devices are heavier', 'C. Blue light can affect sleep patterns', 'D. Physical books are more colorful'],
                    'answer': 'C',
                    'explanation': '文中指出"The blue light emitted by phones and tablets can interfere with our natural sleep cycles."'
                },
                {
                    'question': 'What do employers think about reading skills?',
                    'options': ['A. They are not important', 'B. They are essential skills', 'C. They are only for managers', 'D. They are becoming less important'],
                    'answer': 'B',
                    'explanation': '文中提到"Employers consistently rank reading and writing as essential skills for employees."'
                },
                {
                    'question': 'What is the main idea of this passage?',
                    'options': ['A. Libraries are closing down', 'B. Electronic devices are harmful', 'C. Reading has many benefits for personal and professional life', 'D. Physical books are better than e-books'],
                    'answer': 'C',
                    'explanation': '文章整体讨论了阅读对个人生活（改善记忆、减轻压力）和职业生活（雇主看重）的多方面好处。'
                }
            ],
            'difficulty': '中等',
            'word_count': 298,
            'topic': '教育/阅读'
        },
        {
            'title': 'Climate Change and Its Effects',
            'content': """Climate change is one of the most pressing issues facing our planet today. Scientists have observed that the Earth's average temperature has risen significantly over the past century, primarily due to human activities such as burning fossil fuels and deforestation.

The effects of climate change are already being felt around the world. Rising sea levels threaten coastal communities, while extreme weather events like hurricanes, droughts, and heat waves are becoming more frequent and severe. Agricultural patterns are also changing, affecting food security in many regions.

Governments and organizations are taking action to address this crisis. The Paris Agreement, signed by nearly 200 countries, aims to limit global warming to well below 2 degrees Celsius. Many nations are investing in renewable energy sources like solar and wind power to reduce their carbon emissions.

Individual actions can also make a difference. Simple changes like using public transportation, reducing energy consumption, and eating less meat can help reduce our carbon footprint. Education and awareness are crucial for building a sustainable future.""",
            'questions': [
                {
                    'question': 'What is the main cause of climate change mentioned in the passage?',
                    'options': ['A. Natural weather patterns', 'B. Human activities', 'C. Solar radiation', 'D. Ocean currents'],
                    'answer': 'B',
                    'explanation': '文中明确指出"primarily due to human activities such as burning fossil fuels and deforestation."'
                },
                {
                    'question': 'What is one effect of climate change on agriculture?',
                    'options': ['A. Agricultural patterns are changing', 'B. More crops are being produced', 'C. Farming has become easier', 'D. All regions have better food security'],
                    'answer': 'A',
                    'explanation': '文中提到"Agricultural patterns are also changing, affecting food security in many regions."'
                },
                {
                    'question': 'What is the goal of the Paris Agreement?',
                    'options': ['A. To increase fossil fuel use', 'B. To limit global warming to below 2 degrees Celsius', 'C. To promote deforestation', 'D. To reduce international cooperation'],
                    'answer': 'B',
                    'explanation': '文中说明"The Paris Agreement... aims to limit global warming to well below 2 degrees Celsius."'
                },
                {
                    'question': 'Which of the following is suggested as an individual action to help the environment?',
                    'options': ['A. Driving more cars', 'B. Eating more meat', 'C. Using public transportation', 'D. Increasing energy consumption'],
                    'answer': 'C',
                    'explanation': '文中建议"Simple changes like using public transportation, reducing energy consumption, and eating less meat can help reduce our carbon footprint."'
                }
            ],
            'difficulty': '中等',
            'word_count': 276,
            'topic': '环境/气候变化'
        },
        {
            'title': 'The Importance of Sleep',
            'content': """Sleep is essential for human health and well-being, yet many people do not get enough of it. Adults typically need 7-9 hours of sleep per night, but surveys show that a significant portion of the population regularly sleeps less than 6 hours.

Lack of sleep can have serious consequences. It impairs cognitive function, making it difficult to concentrate and make decisions. Chronic sleep deprivation has been linked to various health problems, including obesity, heart disease, and weakened immune systems. It can also affect mood and increase the risk of accidents.

There are several strategies to improve sleep quality. Maintaining a regular sleep schedule, even on weekends, helps regulate the body's internal clock. Creating a relaxing bedtime routine and keeping bedrooms cool, dark, and quiet can also promote better sleep. Avoiding caffeine and electronic devices in the evening is recommended.

Some people suffer from sleep disorders such as insomnia or sleep apnea. These conditions should be discussed with healthcare providers, as effective treatments are available. Prioritizing sleep is an investment in overall health and quality of life.""",
            'questions': [
                {
                    'question': 'How many hours of sleep do adults typically need per night?',
                    'options': ['A. 4-5 hours', 'B. 7-9 hours', 'C. 10-12 hours', 'D. 5-6 hours'],
                    'answer': 'B',
                    'explanation': '文中明确指出"Adults typically need 7-9 hours of sleep per night."'
                },
                {
                    'question': 'What is one consequence of chronic sleep deprivation mentioned in the passage?',
                    'options': ['A. Improved memory', 'B. Better concentration', 'C. Increased risk of heart disease', 'D. Stronger immune system'],
                    'answer': 'C',
                    'explanation': '文中提到"Chronic sleep deprivation has been linked to various health problems, including obesity, heart disease, and weakened immune systems."'
                },
                {
                    'question': 'What is recommended for improving sleep quality?',
                    'options': ['A. Drinking coffee before bed', 'B. Using electronic devices in bed', 'C. Maintaining a regular sleep schedule', 'D. Sleeping in a warm, bright room'],
                    'answer': 'C',
                    'explanation': '文中建议"Maintaining a regular sleep schedule, even on weekends, helps regulate the body's internal clock."'
                },
                {
                    'question': 'What should people with sleep disorders do?',
                    'options': ['A. Ignore the problem', 'B. Take sleeping pills without consulting doctors', 'C. Discuss with healthcare providers', 'D. Sleep more during the day'],
                    'answer': 'C',
                    'explanation': '文中建议"These conditions should be discussed with healthcare providers, as effective treatments are available."'
                }
            ],
            'difficulty': '中等',
            'word_count': 264,
            'topic': '健康/睡眠'
        }
    ]
  
    # 随机选择一篇阅读材料
    return random.choice(readings)

def generate_html_content(reading, date_str):
    """生成HTML邮件内容"""
  
    # 生成题目HTML
    questions_html = ""
    for i, q in enumerate(reading['questions'], 1):
        questions_html += f"""
        <div class="question">
            <div class="question-text">{i}. {q['question']}</div>
            <div class="options">
                {' | '.join(q['options'])}
            </div>
            <div class="answer">
                <strong>答案：{q['answer']}</strong><br>
                <em>解析：{q['explanation']}</em>
            </div>
        </div>
        """
  
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); color: white; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px; }}
            .header h1 {{ margin: 0; font-size: 28px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; }}
            .info {{ background: #fff3e0; padding: 15px; border-radius: 5px; margin-bottom: 20px; }}
            .info-item {{ display: inline-block; margin-right: 20px; color: #e65100; font-size: 14px; }}
            .article {{ background: #f8f9fa; padding: 25px; border-radius: 5px; margin-bottom: 30px; }}
            .article-title {{ font-size: 20px; font-weight: bold; color: #2c3e50; margin-bottom: 15px; text-align: center; }}
            .article-content {{ color: #555; font-size: 15px; line-height: 1.8; }}
            .questions {{ margin-top: 30px; }}
            .question {{ background: #e3f2fd; padding: 15px; margin-bottom: 15px; border-radius: 5px; border-left: 4px solid #2196f3; }}
            .question-text {{ font-weight: bold; color: #1565c0; margin-bottom: 10px; }}
            .options {{ color: #555; margin-bottom: 10px; }}
            .answer {{ background: #f1f8e9; padding: 10px; border-radius: 3px; margin-top: 10px; color: #33691e; }}
            .footer {{ text-align: center; color: #999; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📚 每日英语阅读</h1>
            <p>{date_str}</p>
        </div>
      
        <div class="info">
            <span class="info-item">📖 难度：{reading['difficulty']}</span>
            <span class="info-item">📝 词数：{reading['word_count']}词</span>
            <span class="info-item">🏷️ 主题：{reading['topic']}</span>
        </div>
      
        <div class="article">
            <div class="article-title">{reading['title']}</div>
            <div class="article-content">{reading['content'].replace(chr(10), '<br><br>')}</div>
        </div>
      
        <div class="questions">
            <h3 style="color: #1565c0; margin-bottom: 20px;">📝 阅读理解题</h3>
            {questions_html}
        </div>
      
        <div class="footer">
            <p>每日英语阅读推送 | 由GitHub Actions自动生成</p>
            <p>适合同等学力英语考试难度</p>
        </div>
    </body>
    </html>
    """
    return html

def send_email(subject, content):
    """发送邮件"""
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
    print("=" * 50)
    print("每日英语阅读推送")
    print("=" * 50)
  
    date_str = datetime.now().strftime("%Y年%m月%d日")
    print(f"日期: {date_str}")
  
    # 获取阅读材料
    print("\n正在获取英语阅读材料...")
    reading = get_reading_material()
    print(f"获取文章: {reading['title']}")
    print(f"难度: {reading['difficulty']}, 词数: {reading['word_count']}")
  
    # 生成邮件内容
    print("正在生成邮件内容...")
    html_content = generate_html_content(reading, date_str)
  
    # 发送邮件
    subject = f"📚 每日英语阅读 - {date_str}"
    print(f"\n正在发送邮件...")
    success = send_email(subject, html_content)
  
    if success:
        print("\n✅ 英语阅读推送成功！")
    else:
        print("\n❌ 英语阅读推送失败！")
        exit(1)

if __name__ == "__main__":
    main()
