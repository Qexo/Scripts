"""
"name": "批量删除PV统计数据",
"description": "用于删除全部PV统计数据",
"path": "scripts/del-all-pv.py",
"author": "Abudu"
"""


counter = 0
all_ = StatisticPV.objects.all()
for i in all_:
    i.delete()
    counter += 1
print("成功删除了{}条PV数据".format(counter))