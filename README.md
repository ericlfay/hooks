# 安装指南

## 安装tslint CLI

'''npm install -g tslint typescript'''

## 安装hooks

1. 将pre-commit.py 保存为 your_project/.git/hooks/pre-commit 
2. 将你的命名规则 写在 tslint.json中 并保存至 .git 同级目录下
3. 激活pre-commit $ chmod +x your_project/.git/hooks/pre-commit

