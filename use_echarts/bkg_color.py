from pyecharts import options as opts
from pyecharts.charts import Pie

data = [("类别A", 30), ("类别B", 20), ("类别C", 50)]

pie = (
    Pie(init_opts=opts.InitOpts(bg_color='black'))
    .add("", data, radius=["30%", "75%"], rosetype="area")
    .set_global_opts(title_opts=opts.TitleOpts(title="南丁格尔玫瑰图示例"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)

pie.render("rose_chart.html")
pie.render("rose_chart.")
