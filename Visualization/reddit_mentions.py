import pandas as pd
import plotly as py
import plotly.graph_objs as go

def main():
    df = pd.read_csv('./basic_analysis/combined_data.csv')
    
    #creating the traces
    trace_irene = go.Scatter(x = df['date'],
                          y = df['number of titles for irene in reddit'],
                          name = "Irene",
                          line = dict(color = '#21B6F4'))

    trace_irma = go.Scatter(x = df['date'],
                          y = df['number of titles for irma in reddit'],
                          name = "Irma",
                          line = dict(color = '#842FCE'))
                                      
    trace_harvey = go.Scatter(x = df['date'],
                          y = df['number of titles for harvey in reddit'],
                          name = "Harvey",
                          line = dict(color = '#2FCE55'))
    
    trace_maria = go.Scatter(x = df['date'],
                          y = df['number of titles for maria in reddit'],
                          name = "Maria",
                          line = dict(color = '#CE422F'))
                                      
    data = [trace_harvey,trace_irene,trace_irma,trace_maria]                                      
    #creating the layout
    layout = dict(
            title = "Comparision of Mentions in Reddit",
            xaxis = dict(
                    title='Days when the Hurricane hit',
                    titlefont=dict(
                            family='Courier New, monospace',
                            size=18,
                            color='#7f7f7f'
                            ),
                            range = ['2017-08-03','2017-10-16']
                            ),
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
    py.offline.plot(fig,filename = "reddit_LG", auto_open=True)

if __name__ == "__main__":
    main()