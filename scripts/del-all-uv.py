"""
"name": "批量删除UV统计数据",
"description": "用于删除全部UV统计数据",
"path": "scripts/del-all-uv.py",
"author": "Abudu"
"""


counter = 0
all_ = StatisticUV.objects.all()
for i in all_:
    i.delete()
    counter += 1
print("成功删除了{}条PV数据".format(counter))