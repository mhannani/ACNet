import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
colors = {
    'color': 'blue',
    'fontSize': 12,
    'fontStyle': 14,
    'fontWeight': 'bold',
    'margin': 50
}
app.layout = html.Div(
    children=[
        html.H2('This is our Project !'),

    ], )


if __name__ == '__main__':
    app.run_server(debug=True)
