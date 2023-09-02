"""
"name": "查询用户列表",
"description": "(实验性)列出所有系统内用户",
"path": "scripts/list_accounts.py",
"author": "Abudu"
"""


from django.contrib.auth.models import User

for user in User.objects.all():
    print(f"{user.username} --- {'管理员' if user.is_staff else '普通用户'}")