import peewee
import pendulum

from app.extensions import pwdb
from peeweext.fields import DatetimeTZField


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