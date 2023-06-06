import pandas as pd


filepath = "评论信息.xlsx"
data = pd.read_excel(filepath, names=["名字", "性别", "等级", "评论内容", "点赞数"], usecols=[0, 1, 2, 3, 4])
# print("数据集有{}条记录。".format(len(data)))
#
# print(data.head())   # 数据查看
#
# data.info()        # 显示数据的详细信息
# print(data[data["评论内容"].isnull()].head())      #查看是否有空数据

# print(data.columns)                  #观察到列名和数据类型
print(data.describe())      #统计分析  查看数据的基本情况，包括：count 非空值数、mean 平均值、std 标准差、max 最大值、min 最小值、（25%、50%、75%）分位数



