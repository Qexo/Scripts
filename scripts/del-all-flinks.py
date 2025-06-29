"""
"name": "批量删除友链",
"description": "用于删除全部的友链申请",
"path": "scripts/del-all-flinks.py",
"author": "Abudu"
"""


counter = FriendModel.objects.filter(status=False).delete()[0]
print("成功删除了{}条友链".format(counter) if counter else "无未通过的友链")