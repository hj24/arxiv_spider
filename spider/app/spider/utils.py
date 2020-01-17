import re


# 爬取arxiv需要的正则匹配模式
PAGNUMPAT = re.compile(r'Showing.*?&ndash;(\d+).*?of.*?(\d+).*?results.*?for.*?all:')

# 解析title
TITLE = re.compile(r'<p.*?class="title is-5 mathjax">\s+(.*?)\s+</p>')

# 解析arx_url
ARXURL = re.compile(r'<a.*?href="(.*?)">arXiv:.*?</a>')

# 解析pdf_url
PDFURL = re.compile(r'<a.*?href="(.*?)">pdf</a>')
