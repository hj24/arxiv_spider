from sea.app import BaseApp


class App(BaseApp):

    def ready(self):
        from app.extensions import spredis
        spredis.set('sp', 'run')
        print('project start!')
