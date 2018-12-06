import plotly
plotly.tools.set_credentials_file(username='anr49', api_key='5lf1HJcMk3GIAs5BcsN7')

import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go
import json


def plot_piechart():
	sent_data = dict()
	with open("all_sent.json") as json_file:
		sent_data = json.load(json_file)

	for source in sent_data:
		labels = []
		values = []
		for key, val in sent_data[source].items():
			labels.append(key)
			values.append(val)
		print(labels)
		print(values)
		graph_title = ""
		if source == "reddit":
			graph_title = "Reddit"
		elif source == "nytimes":
			graph_title = "New York Times"
		elif source == "guardian":
			graph_title = "Guardian"
		trace = go.Pie(labels=labels,
					   values=values,
					   hoverinfo='label+percent', textinfo='percent',
					   title=graph_title)
		py.iplot([trace], filename="{}_sent_piechart".format(source))


def main():
	plot_piechart()
if __name__ == "__main__":
	main()

