# Scripts
Qexo 云端命令库
## 编写命令
1. 在 scripts 目录下创建文件 xxx.py
2. 参考示例(hello-world.py)编辑你的命令，可直接使用 hexoweb/functions.py 内置函数
3. 在 index.json 中添加信息
```jsonc
[
    ...
    {
        "name": "名称",
        "description": "介绍",
        "path": "scripts/xxx.py",
        "author": "Your Name",
        "argv": ["name", ...]  //需要填写的参数
    }
]
```
4. 创建 Pull Request
