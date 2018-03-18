
#Imports
from plotly.offline import plot, iplot
import plotly.graph_objs as go

import plotly
import numpy as np
import pandas as pd
import matplotlib as plt
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.plotly as py
import quandl


# Data

quandl.ApiConfig.api_key = "EvzHu2GEhMsgyzCTaFz6"
dataf2 = quandl.get("FRED/GDP")
dataf3_1 = quandl.get("WIKI/GOOGL")
dataf3_2=quandl.get("BCHARTS/ABUCOINSUSD")


# Figure 1



Label1=["X8","X7","X6","X5"]
Label2=["X4","X3","X2","X1"]


yvalues_1 = [20, 15, 50, 15]
yvalues_2 = [-35,-10, -50,  -15]

tracef1 = go.Bar(x=yvalues_1, y=Label1, name="<b>Negative</b>", orientation = 'h', marker = dict(color = "pink", line=dict(color="black", width=2)))

tracef2 = go.Bar(x=yvalues_2, y=Label2, name="Positive", orientation = 'h', marker = dict(color = "lightblue", line=dict(color="black", width=2)))
layout = dict(barmode = 'group',title="<b>Correlations with employees probability of churn</b>", yaxis=dict(title="Variable"))


merge1 = [tracef1, tracef2]
figure1 = dict(data=merge1, layout=layout)



# Figure 2


data2 = [go.Scatter(x=dataf2.index, y=dataf2.Value, mode="lines", fill="tozeroy")]
layout2=dict(title="<b>US GDP over time</b>")

figure2 = dict(data=data2, layout=layout2)


# Figure 3


dataf3_1["Percent_Change"]=dataf3_1.Open.pct_change()
dataf3_2["Percent_Change"]=dataf3_2.Open.pct_change()

tracef3_1 = go.Box(x=dataf3_1["Percent_Change"], name="<b>Google</b>")
tracef3_2 = go.Box(x=dataf3_2["Percent_Change"], name="<b>Bitcoin</b>")

layout3 =dict(title = "<i>Distribution of price changes</i>")

data3 = [tracef3_2, tracef3_1]
figure3 = dict(data=data3, layout=layout3)



# Figure 4


dataf3_1_1=dataf3_1.iloc[1:5,-1:].round(3)
dataf3_2_1=dataf3_2.iloc[1:5,-1:].round(3)

tableheader= dict(values=["Google","Bitcoin"], align=["left", "center"], font=dict(color="white", size=12), fill=dict(color="blue"))

appendtables=dict(values=[dataf3_1_1.values, dataf3_2_1.values], align=["left", "center"], fill=dict(color=["yellow", "white"]))

tracetable=go.Table(header=tableheader, cells=appendtables)
datatable=[tracetable]

tablelayout=dict(width=500, height=300)

table3=dict(data=datatable, layout=tablelayout)




# Figure 5

Project=[dict(Task="Task 1", Start="2018-01-01", Finish="2018-01-31", Resource='Idea Validation'),
          dict(Task="Task 2", Start="2018-03-01", Finish="2018-04-15", Resource='Team formation'),
          dict(Task="Task 3", Start="2018-04-15", Finish="2018-09-30", Resource='Prototyping')]


colors =[ (0.2, 0.7, 0.3), 'rgb(61,89,171)','rgb(255,153,18)'] 

GanttChart_1= ff.create_gantt(Project, colors=colors, title="Startup Roadmap", index_col='Resource', show_colorbar=True)


