import pendulum
from peewee import chunked

from app.extensions import pwdb
from app.model import Article
from app.utils import spider_local_tz


class Saver:
    """
    爬虫存储器
    """
    def __init__(self):
        self._mod = Article
        self._db = pwdb

    def save_one(self, **kwargs):
        try:
            with self._db.database.atomic():
                ret = (self._mod
                            .insert(**kwargs)
                            .on_conflict(
                                conflict_target=[self._mod.title],
                                update={self._mod.updated_at:
                                            pendulum.now(spider_local_tz)})
                            .execute())
        except Exception:
            return -1
        else:
            return ret

    def save_many(self, source, batch=False, size=999):
        try:
            with self._db.database.atomic():
                if not batch:
                    self._mod.insert_many(source).execute()
                else:
                    for bat in chunked(source, size):
                        self._mod.insert_many(bat).execute()
        except Exception:
            return False
        else:
            return True

    def delete_by_id(self, id):
        try:
            with self._db.database.atomic():
                idx = self._mod.delete().where(self._mod.id == id).execute()
        except Exception:
            return -1
        else:
            return idx

    def __getattr__(self, item):
        return getattr(self._mod, item)
