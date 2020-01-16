import re


# 爬取arxiv需要的正则匹配模式
PAGNUMPAT = re.compile(r'Showing.*?&ndash;(\d+).*?of.*?(\d+).*?results.*?for.*?all:')