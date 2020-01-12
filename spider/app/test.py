from app.extensions import Redis

if __name__ == '__main__':
    import os
    from app import App
    from spider.configs import development

    cfg = development
    root_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


    app = App(root_path, env="development")
    app.config.from_object(cfg)

    print(app.config.get_namespace('REDIS_'))

    r = Redis()
    r.init_app(app)

    r.set('name', 'hj')