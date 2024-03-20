from pyecharts import options as opts
from pyecharts.charts import Pie

import numpy as np

"""
option = {
  title: {
    text: '心理健康疾病患者数据',
    subtext: ' Data',
    left: 'center'
  },
  tooltip: {
    trigger: 'item'
  },
  legend: {
    orient: 'vertical',
    left: 'left'
  },
  series: [
    {
      name: 'Access From',
      type: 'pie',
      radius: '50%',
      data: [
        { value: 374000000, name: '焦虑障碍患者' },
        { value: 264000000, name: '抑郁症患者' },
        { value: 45000000, name: '双相情感障碍患者' },
        { value: 20000000, name: '精神分裂症患者' },
      ],
      emphasis: {
        itemStyle: {
          shadowBlur: 10,
          shadowOffsetX: 0,
          shadowColor: 'rgba(0, 0, 0, 0.5)'
        }
      }
    }
  ]
};
"""
values = [374000000, 264000000, 45000000, 20000000]
names = ['焦虑障碍患者', '抑郁症患者', '双相情感障碍患者', '精神分裂症患者']
data = [(name, value) for name, value in zip(names, values)]

# 创建Pie对象
pie = (
    Pie(init_opts=opts.InitOpts(bg_color='black'))
    .add("", data, radius=["50%", "75%"], rosetype="area")
    .set_global_opts(title_opts=opts.TitleOpts(title="心理健康疾病患者数据",
                                               subtitle='Data',
                                               pos_left='left',
                                               title_textstyle_opts=opts.TextStyleOpts(color='white'), ),
                     legend_opts=opts.LegendOpts(orient='vertical',
                                                 pos_left='left',
                                                 pos_top='center',
                                                 textstyle_opts=opts.TextStyleOpts(color='white'),
                                                 item_gap=20,
                                                 item_height=30,
                                                 item_width=30,
                                                 ),
                     )

    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}",
                                               font_size=20,
                                               font_weight='bold',
                                               font_family='Microsoft YaHei',
                                               color='white',
                                               ))

)

# 生成HTML文件
pie.render("rose_chart.html")
