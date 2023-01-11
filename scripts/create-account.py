from django.contrib.auth.models import User

if not User.objects.filter(username=username).count():
    User.objects.create_user(username=username, password=password)
    print(f"创建用户 {username} 成功")
else:
    print(f"用户 {username} 已存在")
