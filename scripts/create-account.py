"""
"name": "创建子用户",
"description": "(实验性)用于创建子用户",
"path": "scripts/create-account.py",
"author": "Abudu",
"argv": [
    {"name": "username", "placeholder": "用户名"},
    {"name": "password", "placeholder": "密码"},
    {"name": "is_staff", "placeholder": "是否是管理员 填写true/false"}
]
"""


from django.contrib.auth.models import User

if not User.objects.filter(username=username).count():
    if is_staff == "true":
        User.objects.create_superuser(username=username, password=password)
        print(f"创建管理员用户 {username} 成功")
    else:
        User.objects.create_user(username=username, password=password)
        print(f"创建用户 {username} 成功")
else:
    print(f"用户 {username} 已存在")
