<h1 align="center" style="text-align: center">ichat</h1>

## 项目状态

施工中 ~_~

## 简介

微信助手，用于监听微信中的信息，实现对应的任务记录和定时的任务提醒


## 实现思路

> itchat 的[文档地址](https://itchat.readthedocs.io/zh/latest/intro/start/)

基于 itchat 的 api 进行实现，监听微信相关消息，执行对于的命令，响应对应的消息。

## 项目运行

### 更新 requirements.txt

```shell
# 仅在 venv 的环境中使用
pip freeze > requirements.txt
```

### 运行项目

```shell
# 注意本项目仅支持 python3.x
python run.py
```

### 代码模块

项目中的模块都应在 ichat 中进行构建及编写，同时在 test 中完成测试用例的编写， 下面是项目的结构：

```shell
>  tree -L 1

.
├── docs     #项目配置文件夹
├── ichat    #主模块
├── run.py   #项目运行
├── setup.py
└── tests    #单元测试
```

