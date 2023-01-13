"""
"name": "批量通过友链",
"description": "用于通过全部的友链申请",
"path": "scripts/pass-all-flinks.py",
"author": "Abudu"
"""


counter = 0
all_friends = FriendModel.objects.filter(status=False)
for friend in all_friends:
    friend.status = True
    friend.save()
    counter += 1
print("成功通过了{}条友链".format(counter) if counter else "无未通过的友链")