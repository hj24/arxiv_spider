# arxiv 爬虫
- 用sea/gRPC写了一个服务
- 提供了一个控制的接口，见/protos目录下的两个py文件
- 内置了一个定时任务，每周日早上七点半爬取
- 内置了阿布云的代理服务
- 代理和爬虫配置放在数据库中，如何建表见`app.model`文件

## 部署
> 采用docker部署
### step 0 - 环境准备
1. `git pull`本项目到服务器
2. cd到`./spider`目录下 (该目录放置了Dockerfile)
3. 配置好该爬虫服务所需的redis, postgres
### step 1 - 构建服务镜像