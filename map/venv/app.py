import plotly as py
import plotly.graph_objs as go
pyplt = py.offline.plot
# Trace
trace_basic = [go.Bar(
            x = ['丹麦', '冰岛', '印度','奥地利','德国','意大利','日本','比利时','法国','澳大利亚','瑞典','瑞士','美国','英国'],
            y = [7,2,6,6,15,2,10,1,15,3,4,1,6,10],
    )]
# Layout
layout_basic = go.Layout(
            title = '进口药物国家---分析',
            xaxis = go.XAxis(range = [-0.5,13.5], domain = [0,1])
    )
# Figure
figure_basic = go.Figure(data = trace_basic, layout = layout_basic)
# Plot
pyplt(figure_basic, filename='1.html')
