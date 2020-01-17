import re


# 爬取 arxiv 需要的正则匹配模式
PAGNUMPAT = re.compile(r'Showing.*?&ndash;(\d+).*?of.*?(\d+).*?results.*?for.*?all:')

# 解析 title
TITLE = re.compile(r'<p.*?class="title is-5 mathjax">\s+(.*?)\s+</p>')

# 解析 arx_url
ARXURL = re.compile(r'<a.*?href="(.*?)">arXiv:.*?</a>')

# 解析 pdf_url
PDFURL = re.compile(r'<a.*?href="(.*?)">pdf</a>')
