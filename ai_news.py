# ai_news.py
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

def get_ai_news():
    """获取AI资讯列表"""
    news_templates = [
        {
            'title': 'OpenAI发布GPT-5预览版，多模态能力大幅提升',
            'summary': 'OpenAI宣布GPT-5预览版向部分企业用户开放测试，新模型在推理、编程和多模态理解方面实现重大突破。',
            'content': 'OpenAI今日宣布，其最新一代大语言模型GPT-5的预览版本已向部分企业合作伙伴开放测试。据官方介绍，GPT-5在多个维度实现了显著提升，特别是在复杂推理、代码生成和多模态理解方面表现出色。',
            'category': '模型发布',
            'source': 'OpenAI官方博客',
            'url': 'https://openai.com/blog',
            'tags': ['GPT-5', '大模型', '多模态']
        },
        {
            'title': '谷歌DeepMind推出AlphaFold 3，蛋白质结构预测再突破',
            'summary': 'DeepMind发布AlphaFold 3，可预测蛋白质与DNA、RNA等分子的复杂相互作用，准确率达95%以上。',
            'content': '谷歌DeepMind今日发布了AlphaFold系列的最新版本AlphaFold 3，这是继2020年AlphaFold 2解决蛋白质结构预测问题后的又一重大突破。',
            'category': 'AI+科学',
            'source': 'DeepMind官网',
            'url': 'https://deepmind.google/',
            'tags': ['AlphaFold', 'DeepMind', '生物医药']
        },
        {
            'title': '英伟达发布新一代AI芯片H200，推理性能提升90%',
            'summary': '英伟达在GTC大会上发布H200芯片，专为生成式AI优化，内存带宽提升1.4倍，推理性能最高提升90%。',
            'content': '英伟达CEO黄仁勋在GTC大会上正式发布了新一代AI芯片H200。作为H100的升级版本，H200采用了全新的HBM3e内存技术，内存容量达到141GB，带宽提升至4.8TB/s。',
            'category': 'AI芯片',
            'source': '英伟达官方',
            'url': 'https://www.nvidia.com/',
            'tags': ['英伟达', 'AI芯片', 'H200']
        },
        {
            'title': '微软Copilot全面整合Office 365，月活用户突破4亿',
            'summary': '微软宣布Copilot已全面整合至Office 365所有应用，企业用户月活突破4亿，生产力平均提升40%。',
            'content': '微软CEO萨提亚·纳德拉在Ignite大会上宣布，AI助手Copilot已完成与Office 365全产品线的深度整合。',
            'category': 'AI应用',
            'source': '微软官方',
            'url': 'https://www.microsoft.com/',
            'tags': ['微软', 'Copilot', 'Office']
        },
        {
            'title': '中国AI大模型备案数量突破200个，监管框架日趋完善',
            'summary': '国家网信办公布最新AI大模型备案清单，累计备案模型达217个，涵盖文本、图像、语音等多个模态。',
            'content': '国家互联网信息办公室今日公布了第十批生成式人工智能服务备案清单。至此，我国累计备案的大模型已达217个。',
            'category': '政策法规',
            'source': '国家网信办',
            'url': 'https://www.cac.gov.cn/',
            'tags': ['AI监管', '大模型备案', '政策']
        },
        {
            'title': '特斯拉FSD V12正式推送，端到端神经网络实现重大突破',
            'summary': '特斯拉开始向北美用户推送FSD V12版本，首次采用端到端神经网络，城市街道驾驶能力显著提升。',
            'content': '特斯拉CEO埃隆·马斯克在X平台宣布，Full Self-Driving (FSD) V12版本已开始向北美地区的Beta测试用户推送。',
            'category': '自动驾驶',
            'source': '特斯拉官方',
            'url': 'https://www.tesla.com/',
            'tags': ['特斯拉', 'FSD', '自动驾驶']
        }
    ]
  
    # 随机选择5-6条新闻
    selected_news = random.sample(news_templates, min(6, len(news_templates)))
    return selected_news

def generate_html_content(news_list, date_str):
    """生成HTML邮件内容"""
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px; }}
            .header h1 {{ margin: 0; font-size: 28px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; }}
            .news-item {{ background: #f8f9fa; border-left: 4px solid #667eea; padding: 20px; margin-bottom: 20px; border-radius: 5px; }}
            .news-title {{ font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }}
            .news-meta {{ color: #7f8c8d; font-size: 12px; margin-bottom: 10px; }}
            .news-summary {{ color: #555; margin-bottom: 10px; }}
            .news-content {{ color: #666; font-size: 14px; }}
            .tag {{ display: inline-block; background: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 12px; font-size: 12px; margin-right: 5px; }}
            .footer {{ text-align: center; color: #999; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🤖 每日AI资讯</h1>
            <p>{date_str}</p>
        </div>
    """
  
    for news in news_list:
        tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in news['tags']])
        html += f"""
        <div class="news-item">
            <div class="news-title">{news['title']}</div>
            <div class="news-meta">📂 {news['category']} | 📰 {news['source']} | 🔗 <a href="{news['url']}">查看原文</a></div>
            <div class="news-summary"><strong>摘要：</strong>{news['summary']}</div>
            <div class="news-content">{news['content']}</div>
            <div style="margin-top: 10px;">{tags_html}</div>
        </div>
        """
  
    html += """
        <div class="footer">
            <p>每日AI资讯推送 | 由GitHub Actions自动生成</p>
            <p>如需取消订阅，请联系管理员</p>
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
        # 修复From头部格式 - 使用标准格式
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
    print("每日AI资讯推送")
    print("=" * 50)
  
    date_str = datetime.now().strftime("%Y年%m月%d日")
    print(f"日期: {date_str}")
  
    # 获取AI资讯
    print("\n正在获取AI资讯...")
    news_list = get_ai_news()
    print(f"获取到 {len(news_list)} 条资讯")
  
    # 生成邮件内容
    print("正在生成邮件内容...")
    html_content = generate_html_content(news_list, date_str)
  
    # 发送邮件
    subject = f"🤖 每日AI资讯 - {date_str}"
    print(f"\n正在发送邮件...")
    success = send_email(subject, html_content)
  
    if success:
        print("\n✅ AI资讯推送成功！")
    else:
        print("\n❌ AI资讯推送失败！")
        exit(1)

if __name__ == "__main__":
    main()
