import pandas as pd
import plotly as py
import plotly.graph_objs as go

def main():
    df = pd.read_csv('combined_data.csv')
    
    #creating the traces
    trace_reddit = go.Scatter(x = df['date'],
                          y = df['number of titles for maria in reddit'],
                          name = "Reddit mentions",
                          line = dict(color = '#21B6F4'))

    trace_nytimes = go.Scatter(x = df['date'],
                          y = df['number of titles for maria in nytimes'],
                          name = "NYTimes mentions",
                          line = dict(color = '#43D628'))
                                      
    trace_guardian = go.Scatter(x = df['date'],
                          y = df['number of titles for maria in guardian'],
                          name = "Guardian mentions",
                          line = dict(color = '#D63828'))
    data = [trace_nytimes, trace_reddit, trace_guardian]                                      
    #creating the layout
    layout = dict(
            title = "Hurricane Maria",
            xaxis = dict(
                    title='Days when the Hurricane hit',
                    titlefont=dict(
                            family='Courier New, monospace',
                            size=18,
                            color='#7f7f7f'
                            ),
                            range = ['2017-09-02','2017-10-16']),
            yaxis=dict(
                    title='Number of mentions',
                    titlefont=dict(
                            family='Courier New, monospace',
                            size=18,
                            color='#7f7f7f'
        )
            )
                    )
    
    #creating the plot. Currently creating offline cuz no internet, but should 
    #create online to embed. Also change the library name if creating online.
    fig = dict(data=data, layout = layout)
    py.offline.plot(fig,filename = "maria_LG", auto_open=True)

if __name__ == "__main__":
    main()
