# 以Python3.6.3作为基础镜像
FROM python:3.6.3

# 维护者
LABEL maintainer="mambahj24@gmail.com"

# 将项目文件添加到镜像内的spider文件夹
ADD . /spider

# 设置spider目录为工作目录,相当于cd
WORKDIR /spider

# 设置环境变量SEA_ENV, sea根据这个环境变量读取配置
# 这里设置为生成环境的配置
ENV SEA_ENV production

# 将gRPC使用的9001端口暴露出去
EXPOSE 9001

# build镜像时运行的命令，安装vim，以及项目依赖
RUN apt-get update && apt-get install vim -y \
    && apt-get install lsof -y && apt-get clean \
    && pip install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

# docker run构建容器时会运行的命令，用于启动服务
CMD ["sh", "/spider/start_sea.sh"]
