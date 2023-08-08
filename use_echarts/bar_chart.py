from pyecharts import options as opts
from pyecharts.charts import Bar

"""
option = {
 title: {
    text: '患病率（%）',
        left: 'center'
  },
 tooltip: {
    trigger: 'axis',
    axisPointer: {
      type: 'shadow'
    }
  },
  grid: {
    left: '3%',
    right: '4%',
    bottom: '3%',
    containLabel: true
  },
  backgroundColor:"rgba(0,0,0)",
  xAxis: [
    {
      type: 'category',
      data: ['焦虑障碍', '抑郁障碍', '痴呆', '物质依赖', '精神分裂', '双相情感障碍'],
      axisTick: {
        alignWithLabel: true
      }
    }
  ],
  yAxis: [
    {
      type: 'value'
    }
  ],
  series: [
    {
      name: 'Direct',
      type: 'bar',
      barWidth: '60%',
      data: [7.6,6.8,5.6, 4.7, 0.7, 0.6]
    }
  ]
};
"""

values = [7.6, 6.8, 5.6, 4.7, 0.7, 0.6]
names = ['焦虑障碍', '抑郁障碍', '痴呆', '物质依赖', '精神分裂', '双相情感障碍']
data = [(name, value) for name, value in zip(names, values)]

# 创建Bar对象
bar = (
    Bar(init_opts=opts.InitOpts(bg_color='black'))
    .add_xaxis(names)
    .add_yaxis('', values,
               label_opts=opts.LabelOpts(position='top', formatter='{b}%'),
               )
    .set_global_opts(title_opts=opts.TitleOpts(title="患病率（%）",
                                               pos_left='center',
                                               title_textstyle_opts=opts.TextStyleOpts(color='white'), ),
                     legend_opts=opts.LegendOpts(orient='vertical',
                                                 pos_left='left',
                                                 pos_top='center',
                                                 textstyle_opts=opts.TextStyleOpts(color='white'),
                                                 item_gap=20,
                                                 item_height=30,
                                                 item_width=30,
                                                 is_show=False,
                                                 ),
                     xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color='white'),
                                              splitline_opts=opts.SplitLineOpts(is_show=False),),
                     yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(color='white'),
                                              splitline_opts=opts.SplitLineOpts(is_show=True),),
                     )
    .set_series_opts(label_opts=opts.LabelOpts(formatter='{c}%',
                                               position='top',
                                               color='white',
                                               font_size=16))
)

# 生成html文件
bar.render('bar.html')

