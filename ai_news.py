import smtplib
import random
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

# 邮件配置
EMAIL_CONFIG = {
    'sender': '2773343617@qq.com',
    'password': os.environ.get('EMAIL_PASSWORD', ''),
    'receiver': '2773343617@qq.com',
    'smtp_server': 'smtp.qq.com',
    'smtp_port': 465
}

def get_ai_news():
    """AI资讯内容"""
    news_list = [
        {
            'title': 'OpenAI发布GPT-5预览版，多模态能力大幅提升',
            'summary': 'OpenAI宣布GPT-5预览版向部分企业用户开放测试，新模型在推理、编程和多模态理解方面实现重大突破。',
            'category': '模型发布',
            'tags': ['GPT-5', '大模型', '多模态']
        },
        {
            'title': '谷歌DeepMind推出AlphaFold 3，蛋白质结构预测再突破',
            'summary': 'DeepMind发布AlphaFold 3，可预测蛋白质与DNA、RNA等分子的复杂相互作用，准确率达95%以上。',
            'category': 'AI+科学',
            'tags': ['AlphaFold', 'DeepMind', '生物医药']
        },
        {
            'title': 'Anthropic发布Claude 3.5 Sonnet，编程能力超越GPT-4',
            'summary': 'Anthropic发布Claude 3.5 Sonnet，在代码生成、逻辑推理和多语言处理方面表现优异，性价比突出。',
            'category': '模型发布',
            'tags': ['Claude', 'Anthropic', '编程']
        },
        {
            'title': '微软Copilot Studio全面开放，企业可定制专属AI助手',
            'summary': '微软宣布Copilot Studio向所有企业用户开放，支持无代码定制企业专属AI助手，集成Office 365生态。',
            'category': '企业应用',
            'tags': ['微软', 'Copilot', '企业AI']
        },
        {
            'title': 'Stable Diffusion 3开源发布，图像生成质量大幅提升',
            'summary': 'Stability AI开源发布Stable Diffusion 3，采用全新架构，图像生成质量和提示词理解能力显著提升。',
            'category': '开源模型',
            'tags': ['Stable Diffusion', '文生图', '开源']
        },
        {
            'title': '欧盟AI法案正式生效，全球AI监管进入新时代',
            'summary': '欧盟《人工智能法案》正式生效，对高风险AI应用实施严格监管，违规企业最高面临全球营收7%的罚款。',
            'category': '政策法规',
            'tags': ['欧盟', 'AI监管', '合规']
        },
        {
            'title': '英伟达发布H200 GPU，AI算力再创新高',
            'summary': '英伟达发布新一代AI芯片H200，内存带宽和容量大幅提升，为大模型训练和推理提供更强算力支持。',
            'category': 'AI芯片',
            'tags': ['英伟达', 'GPU', '算力']
        }
    ]
    return news_list

def send_email(subject, content):
    """发送邮件"""
    try:
        msg = MIMEMultipart('alternative')
        msg['From'] = Header(f"AI资讯推送 <{EMAIL_CONFIG['sender']}>", 'utf-8')
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
    """主函数"""
    print("=" * 60)
    print("🤖 每日AI资讯推送")
    print(f"📅 {datetime.now().strftime('%Y年%m月%d日 %H:%M')}")
    print("=" * 60)
  
    news_list = get_ai_news()
  
    # 生成HTML邮件内容
    html_content = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{ font-family: 'Microsoft YaHei', Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }}
            .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; }}
            .header h1 {{ margin: 0; font-size: 24px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; }}
            .news-item {{ background: #f8f9fa; padding: 15px; margin-bottom: 15px; border-radius: 8px; border-left: 4px solid #667eea; }}
            .news-title {{ font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 8px; }}
            .news-summary {{ color: #555; margin-bottom: 10px; }}
            .news-meta {{ font-size: 12px; color: #888; }}
            .tag {{ display: inline-block; background: #e3f2fd; color: #1976d2; padding: 2px 8px; border-radius: 12px; margin-right: 5px; font-size: 11px; }}
            .footer {{ text-align: center; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; color: #999; font-size: 12px; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>🤖 每日AI资讯</h1>
            <p>{datetime.now().strftime('%Y年%m月%d日')} | 精选{len(news_list)}条AI行业动态</p>
        </div>
    """
  
    for i, news in enumerate(news_list, 1):
        tags_html = ''.join([f'<span class="tag">{tag}</span>' for tag in news['tags']])
        html_content += f"""
        <div class="news-item">
            <div class="news-title">{i}. {news['title']}</div>
            <div class="news-summary">{news['summary']}</div>
            <div class="news-meta">
                分类: {news['category']} | {tags_html}
            </div>
        </div>
        """
  
    html_content += """
        <div class="footer">
            <p>每日AI资讯推送 | GitHub Actions自动发送</p>
            <p>如不想接收，请取消GitHub仓库的Actions</p>
        </div>
    </body>
    </html>
    """
  
    subject = f"🤖 每日AI资讯 - {datetime.now().strftime('%m月%d日')}"
  
    if send_email(subject, html_content):
        print("✅ AI资讯推送完成！")
    else:
        print("❌ AI资讯推送失败！")

if __name__ == "__main__":
    main()
