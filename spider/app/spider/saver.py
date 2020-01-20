from peewee import chunked

from app.extensions import pwdb
from app.model import Article


class Saver:
    """
    爬虫存储器
    """
    def __init__(self):
        self._mod = Article
        self._db = pwdb

    def save_one(self, **kwargs):
        try:
            with self._db.atomic():
                self._mod.insert(**kwargs).execute()
        except Exception:
            return False
        else:
            return True

    def save_many(self, source, batch=False, size=999):
        try:
            with self._db.atomic():
                if not batch:
                    self._mod.insert_many(source).execute()
                else:
                    for bat in chunked(source, size):
                        self._mod.insert_many(bat).execute()
        except Exception:
            return False
        else:
            return True

    def __getattr__(self, item):
        return getattr(self._mod, item)
