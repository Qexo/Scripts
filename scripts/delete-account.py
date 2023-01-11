from django.contrib.auth import authenticate

user = authenticate(username=username, password=password)
if user is not None:
    if not user.is_staff:
        user.delete()
        print("成功删除用户")
    else:
        print("不支持删除管理员用户")
else:
    print("用户不存在")