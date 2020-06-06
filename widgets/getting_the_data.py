import dash
import dash_core_components as dcc
import dash_html_components as html


def upload():
    return html.Div([
        dcc.Upload(
            html.Div([
                    'drag and drop or  , ',
                    html.A(' Select local file ...', style={'color': 'blue','textDecoration':'underline','cursor':'pointer'}),
            ],
                style={'padding':'40px','margin':'40px',
                       'backgroundColor':'#e8efe9','boderWidth':'2px',
                       'borderRadius':'10px','borderStyle':'dotted'}),

            id='upload_file',

        )
    ], className='center text-center pagination-centered', style={'paddingTop': '100px', 'paddingBottom': '100px'})
