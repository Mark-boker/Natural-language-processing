import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar, Pie
from pyecharts.faker import Faker

filepath = "评论信息.xlsx"
data = pd.read_excel(filepath, names=["名字", "性别", "等级", "评论内容", "点赞数"], usecols=[0, 1, 2, 3, 4])
# print(data['等级'].to_list())
# 使pyechart中的bar对点赞top50进行柱状图可视化呈现，滚动加载
df1 = data.sort_values(by="点赞数", ascending=False).head(20)  # 根据点赞降序排列
print(df1.head(20))

#用pyechart呈现出可以拖动的条形图，灵活呈现该视频的点赞情况
bar = (
    Bar()
    .add_xaxis(df1["评论内容"].to_list())
    .add_yaxis("点赞数", df1["点赞数"].to_list(), color=Faker.rand_color())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="评论热度Top20"),
        datazoom_opts=[opts.DataZoomOpts(), opts.DataZoomOpts(type_="inside")],
    )
    .render("点赞排序.html")
)



# 使用以用户等级为索引，使用value_counts查看每一等级下的用户数，降序
# print(data.等级.value_counts().sort_index(ascending=False))
# pie = (
#     Pie()
#     .add(
#         "",
#         [list(z) for z in zip([str(i) for i in range(7)], (data.等级.value_counts().sort_index(ascending=False)).to_list())],
#         radius=["40%", "75%"],
#     )
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="等级分布"),
#         legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#     .render("用户等级分布.html")
# )
# pie

# 对用户性别分布进行饼图呈现
# print(data.性别.value_counts().sort_index(ascending=False))
#
# pie_gender = (
#     Pie()
#         .add(
#         "",
#         [list(z) for z in zip(["男", "女", "保密"], (data.性别.value_counts().sort_index(ascending=False)).to_list())],
#         radius=["40%", "75%"],
#     )
#         .set_global_opts(
#         title_opts=opts.TitleOpts(title="性别分布"),
#         legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
#     )
#         .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
#         .render("性别分布.html")
#
# )
# pie_gender