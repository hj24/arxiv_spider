from sea.app import BaseApp


class App(BaseApp):

    def ready(self):
        print('sea start!')
