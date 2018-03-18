import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from plotly.offline import plot, iplot
import plotly.graph_objs as go
import plotly.figure_factory as ff
import matplotlib as mpl
import plotly.plotly as py
import numpy as np
import pandas as pd
import quandl

from figures import figure1
from figures import figure2
from figures import figure3
from figures import table3
from figures import GanttChart_1


slider = quandl.get ("FRED/GDP", authtoken = "EvzHu2GEhMsgyzCTaFz6")

app=dash.Dash()

app.css.append_css({"external_url": 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

#Task 1

app.layout=html.Div([

	html.Div([html.H1(children="Homework 5", style={"color":"Green", "text-align":"center", "font-weight":"bold",})],
		className="twelve columns"),

#Task 2

html.Div([
			
			html.Div([

			dcc.RadioItems(id="radio", options=[
            {"label": "Employee Churn", "value": figure1}],
            value="show"),
            dcc.RadioItems(id="radio", options=[
            {"label": "Startup RoadMap", "value": GanttChart_1}],
            value="show")
            ], className="three columns"),
			
			html.Div([
			dcc.Graph(id="Graph")],
			className="nine columns"),

			], className="twelve columns"),



#Task 3,4,5

html.Div([
			html.Div([dcc.Dropdown(
				id = 'stocks',
				options=[
	            {'label': 'Google', 'value': 'GOOGL'},
	            {'label': 'Amazon.com', 'value': 'AMZN'},
	            {'label': 'Vodafone', 'value': 'CAGR'},
	            {'label': 'Lenovo', 'value': '00992'},
	            {'label': 'Walmart', 'value': 'WMT'}
			],
				placeholder='Please, select a stock', multi=True),
				html.Button(id='submit',n_clicks=0, children='Submit'),
			],	className="two columns"),

			html.Div([
			dcc.Graph(id="box-plot")],
			className="five columns"),

			html.Div([
			dcc.Graph(id="table")],
			className="five columns"),

			], className="twelve columns"),



#Task 6

html.Div([
	html.Div([dcc.RangeSlider(id = 'option_in', min=0, max=len(slider.index), value= [0, len(slider.index)])],
	className= 'four columns'),

	html.Div([dcc.Graph(id='GDP')],
		className= 'eight columns'),
	], className= 'twelve columns',)


])

#Radio Button callback

@app.callback(
    Output(component_id="Graph", component_property="figure"),
    [Input(component_id="radio", component_property="value")])
	
def update_graph(Inputvalue):
	figure=Inputvalue
	return figure



#Dropdown Callback

@app.callback(
    Output(component_id='box-plot', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='stocks', component_property='value')])

def update_graph(clicks, input_value1):
	quandlinput1 = "WIKI/"+input_value1[0]
	quandlinput2 = "WIKI/"+input_value1[1]
	
	stock1 = quandl.get(quandlinput1, authtoken = "EvzHu2GEhMsgyzCTaFz6")
	stock2 = quandl.get(quandlinput2, authtoken = "EvzHu2GEhMsgyzCTaFz6")
	
	x1 = stock1.Open.pct_change()
	x2 = stock2.Open.pct_change()
	
	trace1 = go.Box(x=x1, name=input_value1[0])
	trace2 = go.Box(x=x2, name=input_value1[1])
	
	layout3 = dict(title="<i>Distribution of Price changes</i> "+input_value1[0]+" and "+input_value1[1])
	data3 = [trace1,trace2]
	figure = dict(data=data3, layout=layout3)
	return figure

#Table Callback

@app.callback(
    Output(component_id='table', component_property='figure'),
    [Input(component_id='submit', component_property='n_clicks')],
    [State(component_id='stocks', component_property='value')]
)

def update_table(clicks, inputvalue2):

	quandlinput3 ="WIKI/"+inputvalue2[0]
	quandlinput4 = "WIKI/"+inputvalue2[1]
	
	stock3 = quandl.get(quandlinput3, authtoken = "EvzHu2GEhMsgyzCTaFz6")
	stock4 = quandl.get(quandlinput4, authtoken = "EvzHu2GEhMsgyzCTaFz6")

	stockdata3["%C"] = stock3.Open.pct_change()
	stockdata4["%C"] = stock4.Open.pct_change()
	
	stockdata_3=stockdata3.iloc[1:5,-1:].round(3)
	stockdata_4=stockdata4.iloc[1:5,-1:].round(3)

	header= dict(values=[inputvalue2[0],inputvalue2[1]],
				align=["left", "center"],
				font=dict(color="white", size=12),
				fill=dict(color="#119DFF"),
				)


	cells = dict(values=[stockdata_3.values, stockdata_4.values],
             align=["left", "center"],
             fill=dict(color=["yellow", "white"]))

	trace4 = go.Table(header=header, cells=cells)

	data4 = [trace4]

	layout4=dict(width=500, height=300)

	figure=dict(data=data4, layout=layout4)

	return figure


#Slider Callback


@app.callback(
    Output(component_id='GDP', component_property='figure'),
    [Input(component_id='option_in', component_property='value')]
)
def update_graph(Input_value):
	sindex = slider.index[Input_value[0]: Input_value[1]]
	svalues = slider.Value[Input_value[0]: Input_value[1]]

	datas = [go.Scatter(x= sindex, y=svalues, fill='tozeroy')]
	layout = dict (title = 'US GDP')
	figure = dict (data=datas, layout= layout)
	return figure




if __name__ == '__main__':
	app.run_server(debug=True)
