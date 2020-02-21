from sea.app import BaseApp


class App(BaseApp):

    def ready(self):
        from app.extensions import spredis
        spredis.set('sp', 'run')
        print('project start!')

def register(sender):
    # https://www.cnblogs.com/yuzhenjie/p/9398569.html
    import consul
    from sea import current_app
    cfg = current_app.config.get_namespace("CONSUL_")
    c = consul.Consul(host=cfg["server_host"])
    server_name = cfg["server_name"]
    ip = cfg["register_ip"]
    port = cfg["register_port"]
    print(f"开始注册服务{server_name}")
    # 健康检查的ip，端口，检查时间
    check = consul.Check.tcp(ip, port, "10s")
    # 注册服务部分
    c.agent.service.register(server_name, f"{server_name}",
                            address=ip, port=port, check=check) 
    print(f"注册服务{server_name}成功")

def unregister(sender):
    import consul
    from sea import current_app
    cfg = current_app.config.get_namespace("CONSUL_")
    c = consul.Consul(host=cfg["server_host"])
    server_name = cfg["server_name"]
    print(f"开始退出服务{server_name}")
    c.agent.service.deregister(f'{server_name}')

# 接收到server创建的信号时注册服务
from sea.signals import server_stopped, server_started
server_started.connect(register)
server_stopped.connect(unregister)
