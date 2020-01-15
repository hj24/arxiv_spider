import peewee
import pendulum
from peeweext.fields import JSONCharField
from peeweext.fields import DatetimeTZField

from app.extensions import pwdb


class ProxyConfiguration(pwdb.Model):
    """
    爬虫代理配置表
    """
    puser = peewee.CharField(max_length=25)
    pwd = peewee.CharField(max_length=25)
    host = peewee.CharField(max_length=25)
    port = peewee.CharField(max_length=10)
    ptype = peewee.IntegerField()
    deleted = peewee.BooleanField()
    created_at = DatetimeTZField(default=pendulum.now)
    updated_at = DatetimeTZField(default=pendulum.now)

    class Meta:
        table_name = 'proxy_configuration'

class SpConfiguration(pwdb.Model):
    """
    爬虫配置表
    """
    sleep = peewee.CharField(max_length=10)
    interval = peewee.CharField(max_length=10)
    headers = peewee.TextField()
    timeout = peewee.IntegerField()
    deleted = peewee.BooleanField()
    created_at = peewee.DateTimeField(default=pendulum.now)
    updated_at = peewee.DateTimeField(default=pendulum.now)

    class Meta:
        table_name = 'sp_configuration'

class Api(pwdb.Model):
    """
    爬出需要的母api表，根据爬取它的结果生成子api
    """
    url = peewee.CharField(max_length=100)
    payload = JSONCharField(max_length=300)
    apitype = peewee.IntegerField()
    accesstype = peewee.IntegerField()
    deleted = peewee.BooleanField()
    created_at = peewee.DateTimeField(default=pendulum.now)
    updated_at = peewee.DateTimeField(default=pendulum.now)

    class Meta:
        table_name = 'sp_apilist'

class Article(pwdb.Model):
    """
    文章模型，用于存储爬取的文章
    """
    author = peewee.CharField(max_length=80)
    title = peewee.CharField(max_length=100)
    subject = peewee.CharField(max_length=60)
    arx_url = peewee.CharField(max_length=150)
    pdf_url = peewee.CharField(max_length=150)
    expr = peewee.CharField(max_length=200)
    content = peewee.TextField()
    fav_num = peewee.IntegerField()
    downloaded = peewee.BooleanField()
    created_at = peewee.DateTimeField(default=pendulum.now)
    updated_at = peewee.DateTimeField(default=pendulum.now)

    class Meta:
        table_name = 'fb_article'
