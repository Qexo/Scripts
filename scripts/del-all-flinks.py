"""
"name": "批量删除友链",
"description": "用于删除全部的友链申请",
"path": "scripts/del-all-flinks.py",
"author": "Abudu"
"""


counter = 0
all_friends = FriendModel.objects.filter(status__in=[False])
for friend in all_friends:
    friend.delete()
    counter += 1
print("成功删除了{}条友链".format(counter) if counter else "无未通过的友链")