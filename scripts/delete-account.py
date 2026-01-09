"""
"name": "删除子用户",
"description": "(实验性)用于删除子用户",
"path": "scripts/delete-account.py",
"author": "Abudu",
"argv": [
    {"name": "username", "placeholder": "用户名"}
]
"""

from django.contrib.auth.models import User

user = User.objects.filter(username=username).first()
if user is not None:
    #if User.objects.filter(is_staff=True).count() or not user.is_staff:  #Failes
    if User.objects.filter(is_staff__in=[True]).count() > 1 or not user.is_staff:  # Works 
        user.delete()
        print("成功删除用户")
    else:
        print("至少需要一个管理员账户")
else:
    print("用户不存在")