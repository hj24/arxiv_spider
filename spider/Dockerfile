# 以Python3.6.3作为基础镜像
FROM python:3.6.3

# 维护者
MAINTAINER mambahj24@gmail.com

# 将项目文件添加到镜像内的spider文件夹
ADD . /spider

# 设置spider目录为工作目录,相当于cd
WORKDIR /spider

# 设置环境变量SEA_ENV, sea根据这个环境变量读取配置
# 这里设置为生成环境的配置
ENV SEA_ENV production

# build镜像时运行的命令，安装vim，以及项目依赖
RUN apt-get update && apt-get install vim -y && apt-get clean \
    && pip install -r requirements.txt

# docker run构建容器时会运行的命令，用于启动服务
CMD ["/bin/sh", "start_sea.sh"]
