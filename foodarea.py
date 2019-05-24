import pandas as pd
from pyecharts.charts import Pie, Bar, Page
from pyecharts import options as opts

# pie 饼图

# 从csv文件中过滤我要分析并绘图的数据
# 统计指定区域的美食店铺的情况
def foodDatas(city):
    # 读取数据
    df = pd.read_csv('food.csv', encoding='utf-8-sig')
    datas = df[df['所在的城市'] == city].groupby('区域')

    fdata = [] # [(,),(,)]
    for item in datas:
        # 注意 饼图的数据在拼接时候都需要使用 字符串 这个和之前的0.5的版本有差异
        fdata.append((item[0], str(item[1]['区域'].count())))

    # 绘图
    pie = Pie()
    pie.add('', fdata,radius=['35%', '40%'],center=['50%', '55%'])
    pie.set_global_opts(title_opts=opts.TitleOpts(title=city+'店铺统计', pos_left='center'),
                        legend_opts=opts.LegendOpts(orient='vertical', pos_top='15%', pos_left='2%'),
                        toolbox_opts=opts.ToolboxOpts()
                        )
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}:{c}"))

    # pie.render()

    # 柱状图

    bar = Bar()
    # 数据组织
    # print(fdata)
    x_data = []
    y_data = []

    [x_data.append(i[0]) for i in fdata]
    # for i in fdata:
    #     x_data.append(i[0])
    [y_data.append(int(i[1])) for i in fdata]

    bar.add_xaxis(x_data)
    bar.add_yaxis(city,y_data)
    # bar.add_yaxis('北京', y_data)
    print(x_data)
    print(y_data)

    bar.set_global_opts(title_opts=opts.TitleOpts(title=city + '区域店铺数据',subtitle='2019.5.23'),
                        xaxis_opts=opts.AxisOpts(name='区域名称'),
                        yaxis_opts=opts.AxisOpts(name='店铺统计'),
                        toolbox_opts=opts.ToolboxOpts(),
                        legend_opts=opts.LegendOpts(is_show=False)
                        )
    bar.set_series_opts(
        label_opts=opts.LabelOpts(is_show=False),
        markpoint_opts=opts.MarkPointOpts(

            data=[
                opts.MarkPointItem(type_='max',name='最大值'),
                opts.MarkPointItem(type_='min',name='最小值'),
                opts.MarkPointItem(type_='average',name='平均值')
            ]
        )
    )

    # bar.render()

    page = Page()
    page.add(pie)
    page.add(bar)
    page.render('foodarea.html')









if __name__ == '__main__':
    # 组织数据
    foodDatas('上海')




