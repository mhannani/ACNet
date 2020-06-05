import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(id='div', children=[

    dbc.Alert("This is a primary alert", color="primary", id="center"),
    html.Div(children='Dash is a web application framework for python'),
    dcc.Graph(
        id="graph example",
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [6, 2, 1], 'type': 'bar', 'name': 'SF'},
                {}

            ]
        }

    ),
]

                      )

if __name__ == '__main__':
    app.run_server(debug=True)
