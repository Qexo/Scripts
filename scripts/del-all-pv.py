"""
"name": "批量删除PV统计数据",
"description": "用于删除全部PV统计数据",
"path": "scripts/del-all-pv.py",
"author": "Abudu"
"""


counter = StatisticPV.objects.count()
StatisticPV.objects.all().delete()
print("成功删除了{}条PV数据".format(counter))