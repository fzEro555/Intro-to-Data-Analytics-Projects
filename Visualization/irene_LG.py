import pandas as pd
import plotly as py
import plotly.graph_objs as go

def main():
    df = pd.read_csv('combined_data.csv')
    
    #creating the traces
    trace_reddit = go.Scatter(x = df['date'],
                          y = df['number of titles for irene in reddit'],
                          name = "Reddit mentions",
                          line = dict(color = '#21B6F4'))

    trace_nytimes = go.Scatter(x = df['date'],
                          y = df['number of titles for irene in nytimes'],
                          name = "NYTimes mentions",
                          line = dict(color = '#43D628'))
                                      
    trace_guardian = go.Scatter(x = df['date'],
                          y = df['number of titles for irene in guardian'],
                          name = "Guardian mentions",
                          line = dict(color = '#D63828'))
    data = [trace_nytimes, trace_reddit, trace_guardian]                                      
    #creating the layout
    layout = dict(
    title = "Hurricane Irene",
    xaxis = dict(
        range = ['2011-08-07','2011-09-11']))
    
    #creating the plot. Currently creating offline cuz no internet, but should 
    #create online to embed. Also change the library name if creating online.
    fig = dict(data=data, layout = layout)
    py.offline.plot(fig,filename = "irene_LG", auto_open=True)

if __name__ == "__main__":
    main()
