import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

df = pd.DataFrame(
    {
        "Fruit": [
            "Apples",
            "Oranges",
            "Bananas",
            "Apples",
            "Oranges",
            "Bananas",
            "Trees"
        ],
        "Amount": [4, 1, 2, 2, 4, 5,8],
        "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal","Seoul"],
    }
)

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(
    children=[
        html.H1(
            children='Hello Dash',
            style={
            'textAlign': 'center',
            'color': colors['text']
            }
            ),
        html.Div(
            children='''
        Dash: A web application framework for your data.
    '''
        ),
        dcc.Graph(id='example-graph', figure=fig),
        html.H2("Hello - Second")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
