"""
"name": "批量通过友链",
"description": "用于通过全部的友链申请",
"path": "scripts/pass-all-flinks.py",
"author": "Abudu"
"""


counter = FriendModel.objects.filter(status=False).update(status=True)
print("成功通过了{}条友链".format(counter) if counter else "无未通过的友链")