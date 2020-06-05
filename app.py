import os

import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.Div([
        ## first row : ##
        html.Div([
            # Dropdown menu :
            dcc.Dropdown(
                options=[
                    {'label': 'option_1', 'value': 'value_1'},
                    {'label': 'option_2', 'value': 'value_2'},
                    {'label': 'option_3', 'value': 'value_2'}
                ],
                value='value_3'  # The default selected value
            )
        ], className="four columns"),
        html.Div([
            ## Dropdown with multi-selction:
            dcc.Dropdown(
                options=[
                    {'label': 'option_1', 'value': 'value_1'},
                    {'label': 'option_2', 'value': 'value_2'},
                    {'label': 'option_3', 'value': 'value_2'}
                ],
                multi=True,
            )
        ], className="four columns"),
        html.Div([
            ## Radioitems :
            dcc.RadioItems(
                options=[
                    {'label':'Radio_1','value':'Radio_1'},
                    {'label':'Radio_2','value':'Radio_2'},
                    {'label':'Radio_3','value':'Radio_3'}
                ],
                value='Radio_1',
            )
        ], className="four columns")
    ], className="row"),
    html.Div([
        ## second row : ##
        html.Div([
            ##Checkboxes :
            dcc.Checklist(
                options=[
                    {'label':'checklist_1','value':'checklist_1'},
                    {'label':'checklist_2','value':'checklist_2'},
                    {'label':'checklist_3','value':'checklist_3'}
                ],
            )
        ], className="four columns"),
        html.Div([
            ##Slider:
            dcc.Slider(
                min=0,
                max=4,
                marks={i:str(i/10.0) for i in range(0,5,1)},
                value=4,
            ),
        ], className="four columns"),
    ], className="row"),
], className="container-xl")


if __name__ == '__main__':
    app.run_server(debug=True)
