# stock_news.py
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

def get_stock_news():
    """获取股市资讯列表"""
    news_templates = [
        {
            'title': 'A股三大指数集体收涨，北向资金净流入超50亿元',
            'summary': '今日A股三大指数全线飘红，沪指涨0.8%，深成指涨1.2%，创业板指涨1.5%，北向资金净流入52.3亿元。',
            'content': '今日A股市场表现强劲，三大指数集体收涨。截至收盘，上证指数报3050.32点，上涨0.8%；深证成指报9788.65点，上涨1.2%；创业板指报1923.45点，上涨1.5%。两市成交额达9800亿元，较上一交易日放量1200亿元。',
            'category': '市场综述',
            'source': '证券时报',
            'url': 'http://www.stcn.com/',
            'tags': ['A股', '北向资金', '大盘']
        },
        {
            'title': '美联储暗示年内可能降息，全球股市应声上涨',
            'summary': '美联储会议纪要显示多数官员支持年内降息，市场预期6月启动降息周期，全球主要股市集体走高。',
            'content': '美联储公布的最新会议纪要显示，多数联邦公开市场委员会（FOMC）成员认为，如果通胀数据继续向好，2024年启动降息是合适的。这一表态强化了市场对降息的预期。',
            'category': '宏观政策',
            'source': '华尔街见闻',
            'url': 'https://wallstreetcn.com/',
            'tags': ['美联储', '降息', '美股']
        },
        {
            'title': '新能源汽车板块强势领涨，比亚迪股价创历史新高',
            'summary': '新能源汽车概念股今日表现亮眼，板块整体涨幅达3.5%，比亚迪股价突破300元关口，市值重回8000亿元。',
            'content': '新能源汽车板块今日成为市场最大亮点。在政策支持叠加销量超预期的双重利好下，板块整体上涨3.5%。龙头比亚迪股价大涨5.2%，报302.56元，创历史新高，市值突破8000亿元。',
            'category': '行业动态',
            'source': '财联社',
            'url': 'https://www.cls.cn/',
            'tags': ['新能源汽车', '比亚迪', '锂电池']
        },
        {
            'title': '央行开展1000亿元MLF操作，利率维持不变',
            'summary': '为维护银行体系流动性合理充裕，央行今日开展1000亿元中期借贷便利（MLF）操作，中标利率维持2.5%不变。',
            'content': '中国人民银行今日发布公告，为维护银行体系流动性合理充裕，开展1000亿元中期借贷便利（MLF）操作，期限1年，中标利率2.5%，与上期持平。今日有4990亿元MLF到期。',
            'category': '货币政策',
            'source': '央行官网',
            'url': 'http://www.pbc.gov.cn/',
            'tags': ['央行', 'MLF', '货币政策']
        },
        {
            'title': '科技股集体走强，半导体板块掀涨停潮',
            'summary': '受AI芯片需求旺盛提振，半导体板块今日大涨4.2%，中芯国际、北方华创等多只个股涨停。',
            'content': '科技板块今日表现强势，半导体、芯片概念股掀起涨停潮。中芯国际涨10%，北方华创涨10%，韦尔股份涨8.5%。市场分析认为，AI算力需求持续高增是主要催化剂。',
            'category': '板块热点',
            'source': '上海证券报',
            'url': 'https://www.cnstock.com/',
            'tags': ['半导体', '芯片', '科技股']
        },
        {
            'title': '证监会发布新规，强化上市公司现金分红监管',
            'summary': '证监会就《上市公司现金分红指引》征求意见，要求连续三年分红比例低于30%的公司说明原因。',
            'content': '中国证监会今日发布《上市公司现金分红指引（征求意见稿）》，进一步强化上市公司现金分红监管。指引要求，最近三个会计年度累计现金分红比例低于年均净利润30%的公司，需在年报中详细说明原因。',
            'category': '政策法规',
            'source': '证监会官网',
            'url': 'http://www.csrc.gov.cn/',
            'tags': ['证监会', '分红', '监管']
        }
    ]
  
    # 随机选择5-6条新闻
    selected_news = random.sample(news_templates, min(5, len(news_templates)))
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
            .header {{ background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%); color: white; padding: 30px; border-radius: 10px; text-align: center; margin-bottom: 30px; }}
            .header h1 {{ margin: 0; font-size: 28px; }}
            .header p {{ margin: 10px 0 0 0; opacity: 0.9; }}
            .news-item {{ background: #f8f9fa; border-left: 4px solid #11998e; padding: 20px; margin-bottom: 20px; border-radius: 5px; }}
            .news-title {{ font-size: 18px; font-weight: bold; color: #2c3e50; margin-bottom: 10px; }}
            .news-meta {{ color: #7f8c8d; font-size: 12px; margin-bottom: 10px; }}
            .news-summary {{ color: #555; margin-bottom: 10px; }}
            .news-content {{ color: #666; font-size: 14px; }}
            .tag {{ display: inline-block; background: #e8f5e9; color: #2e7d32; padding: 2px 8px; border-radius: 12px; font-size: 12px; margin-right: 5px; }}
            .footer {{ text-align: center; color: #999; font-size: 12px; margin-top: 30px; padding-top: 20px; border-top: 1px solid #eee; }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 每日股市资讯</h1>
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
            <p>每日股市资讯推送 | 由GitHub Actions自动生成</p>
            <p>投资有风险，入市需谨慎</p>
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
    print("每日股市资讯推送")
    print("=" * 50)
  
    date_str = datetime.now().strftime("%Y年%m月%d日")
    print(f"日期: {date_str}")
  
    # 获取股市资讯
    print("\n正在获取股市资讯...")
    news_list = get_stock_news()
    print(f"获取到 {len(news_list)} 条资讯")
  
    # 生成邮件内容
    print("正在生成邮件内容...")
    html_content = generate_html_content(news_list, date_str)
  
    # 发送邮件
    subject = f"📊 每日股市资讯 - {date_str}"
    print(f"\n正在发送邮件...")
    success = send_email(subject, html_content)
  
    if success:
        print("\n✅ 股市资讯推送成功！")
    else:
        print("\n❌ 股市资讯推送失败！")
        exit(1)

if __name__ == "__main__":
    main()
