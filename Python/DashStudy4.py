from dash import Dash, html, dcc, dash_table, Input, Output, State
import plotly.express as px
import pandas as pd

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

LineList = ["KFBJ","KFBH","KFE5"]
DeviceList = ["KA","KS","LA"]
StepList = ["KA150300","KA150400","KA150600","KS150300","LA150300"]    
ItemList = ['CD1','CD2','CD3','AVG','UNIF']

app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.Div(
            children=[
            html.Label("LINE"),
            dcc.Dropdown(LineList, id = 'LineDropDown'),
            html.Br(),
            html.Label("Device"),
            dcc.Dropdown(DeviceList, id = 'DeviceDropDown')
            ], style={'padding': 10, 'flex': 0.3}),
    
        html.Div(
            children=[
            html.Label("STEP"),
            dcc.Dropdown(StepList, id = 'StepDropDown'),
            html.Br(),
            html.Label("ITEM"),
            dcc.Dropdown(ItemList,multi=True, id = 'ItemDropDown'),
            html.Br(),
            html.Br(),
            html.Button('Search', id='search_button', n_clicks=0, style={'width':'80%','height':'10%'}),
            ], style={'padding': 10, 'flex': 0.3}),     
        
        html.Div( 
            children=[
                html.Div(id='search_input'),
                ], style={'padding': 10, 'flex': 0.3}
            ),
        html.Br(),
        dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns],
                             style_table={'height': '300px','width' : '700px', 'overflowY': 'auto', 'margin-left' : '50px'})
        ], style={'display': 'flex', 'flex-direction': 'row'}),
    
    html.Br(),
    html.Button('Submit', id='subimt_button',
                style ={'width':'10%','height':'40px', 'float':'right', 'margin-right':'100px'}),
    

    html.Div(children=[
        html.Label("Graph"),
        dcc.Graph(id='graph')
        ], style={'flex' : 0.8, 'margin-top':'50px'})
    
    ])


@app.callback(
    Output('search_input', 'children'),
    Input('search_button', 'n_clicks'),
    State('LineDropDown', 'value'),
    State('DeviceDropDown', 'value'),
    State('StepDropDown', 'value'),
    State('ItemDropDown', 'value')
    )
def update_output(n_clicks, input1, input2, input3, input4):
    return u'''Line : "{}",
        Device : "{},
        Step : "{},
        Item : "{}"'''.format(input1, input2, input3, input4)
    
@app.callback(
    Output('graph', 'figure'),
    Input('subimt_button', 'n_clicks'),
    prevent_initial_call=True)
def draw_graph(input5):
    return fig
      
    
if __name__ == '__main__':
    app.run_server(debug=False)
