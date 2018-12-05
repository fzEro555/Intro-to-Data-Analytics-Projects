import plotly
plotly.tools.set_credentials_file(username = 'fzEro5', api_key = 'JW2fEOORvG6eByCT2TfG')
import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

def plot_hypo2():
    df = pd.read_csv("combined_data.csv")

    data = [
            go.Scatter(
                x=df['date'], # assign x as the dataframe column 'x'
                y=df['number of summaries for irma in reddit'],
                name='number of summaries for irma in reddit'
            ),
            go.Scatter(
                x=df['date'], # assign x as the dataframe column 'x'
                y=df['number of summaries for maria in reddit'],
                name='number of summaries for maria in reddit'
            ),
            go.Scatter(
                x=df['date'], # assign x as the dataframe column 'x'
                y=df['number of summaries for harvey in reddit'],
                name='number of summaries for harvey in reddit'
            ),
            go.Scatter(
                x=df['date'], # assign x as the dataframe column 'x'
                y=df['number of summaries for irene in reddit'],
                name='number of summaries for irene in reddit'
            )
            ]
    url = py.plot(data, filename='hypothesis2')

if __name__ == "__main__":
    plot_hypo2()