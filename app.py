import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_scripts = ['https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js',
                    'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js',
                    ]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SKETCHY], external_scripts=external_scripts)
app.layout = html.Div([
#---------------------------------------------------Navbar--------------------------------------------------------------
    html.Nav([
        html.A([
            'Logo'
        ], href='https://acnet.herokuapp.com/', className='navbar-brand'),
        html.Div([
            html.Ul([
                html.Li([
                    html.A([
                        'Home',
                    ], className='nav-link')
                ], className='nav-item'),
                html.Li([
                    html.A([
                        'Feature',
                    ], className='nav-link')
                ], className='nav-item'),

                html.Li([
                    html.A([
                        'About',
                    ], className='nav-link')
                ]),

            ], className='navbar-nav mr-auto'),
            html.Div([
                html.A([
                    html.Span([
                        html.Img(src='assets/img/github.png', style={'height': '35px'}),
                    ], className='float-right'),
                ], target='_Blank', href='https://github.com/SIMOHANNANI/ACNet/')
            ], className='form-inline my-2 my-lg-0'),
        ], className='collapse navbar-collapse'),

    ], className='mt-3 navbar navbar-expand-sm navbar-light bg-light'),
# --------------------------------------------------------Tabs----------------------------------------------------------
    html.Div([
        dbc.Card([
            dbc.CardHeader([
                dbc.Tabs([
                    dbc.Tab(label='getting the data', tab_id='getting_the_data'),
                    dbc.Tab(label='viewing the data', tab_id='viewing_the_data',className='nav-item'),
                    dbc.Tab(label='visualizing the data', tab_id='visualizing_the_data',className='nav-item'),
                ], id='card_tabs', card=True, active_tab='getting_the_data',className='nav nav-pills nav-fill'),
            ]),
            dbc.CardBody([
                # The content of each tab goes here !
            ],id='card_body')

        ], className='mt-5'),
    ],className='ml-5 mr-5'),
],className='ml-4 mr-4')

getting_the_data = 'getting_the_data'
viewing_the_data = 'viewing_the_data'
visualizing_the_data = 'visualizing_the_data'
@app.callback(
    Output(component_id='card_body',component_property='children'),
    [Input(component_id='card_tabs',component_property='active_tab')],

)
def show_tab_content(active_tab):
    if active_tab == 'getting_the_data':
        return getting_the_data
    elif active_tab == 'viewing_the_data':
        return viewing_the_data
    else:
        return visualizing_the_data

if __name__ == '__main__':
    app.run_server(debug=True)
