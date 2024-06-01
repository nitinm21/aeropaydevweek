import os
from dash import Dash, html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import dash
import dash_core_components as dcc


from embedchain import App
# pip install -r requirements.txt

# Create a bot instance
os.environ["OPENAI_API_KEY"] = "sk-proj-W2HVhrM7Z90flfQcaAJ8T3BlbkFJ3k6Z6ZZJwtRKeriUJUau"
ai_bot = App.from_config(config_path="config.yaml")


# Embed resources: websites, PDFs, videos
#ai_bot.add("https://blog.hubspot.com/website/simple-website-examples")
ai_bot.add("https://www.ssa.gov/pubs/EN-05-10181.pdf", data_type='pdf_file')
ai_bot.add("https://ois.uic.edu/life-at-uic/practical-matters/social-security-number-and-itin/")


# ai_bot.add("https://nycaudubon.org/our-work/conservation/project-safe-flight")
# ai_bot.add("Birds Flying Into Windows.pdf", data_type='pdf_file')
# ai_bot.add("https://www.youtube.com/watch?v=l8LDTRxc0Bc")
"""
Basic UI
app = Dash()
app.layout = html.Div([
    html.H1('SSN Bot'),
    html.H3('Ask away all questions related to your SSN'),
    html.Label('Go ahead:'),
    html.Br(),
    dcc.Textarea(id='question-area', value=None, style={'width': '25%', 'height': 100}),
    html.Br(),
    html.Button(id='submit-btn', children='Submit'),
    dcc.Loading(id="load", children=html.Div(id='response-area', children='')),
])
"""

"""
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('SSN Bot'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.H3('Ask away all questions related to your SSN'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Label('Go ahead:'),
            dcc.Textarea(id='question-area', value='', style={'width': '100%', 'height': 100}),
            html.Br(),
            dbc.Button('Submit', id='submit-btn', color='primary'),
            html.Br(),
            dcc.Loading(id="load", children=html.Div(id='response-area')),
        ], width=12)
    ])
], fluid=True)
"""


"""
[working]
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1('SSN Bot', className='text-center my-3'), width=12)
    ),
    dbc.Row(
        dbc.Col(html.H3('Ask any question about getting your SSN', className='text-center'), width=12)
    ),
    dbc.Row(
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Go ahead:', className='card-title'),
                    dcc.Textarea(id='question-area', value='', style={'width': '100%', 'height': '100px', 'resize': 'none'}),
                    html.Br(),
                    dbc.Button('Submit', id='submit-btn', color='primary', className='my-2'),
                ])
            ], className='my-3'),
            dcc.Loading(
                dbc.Card(id="load", children=[
                    dbc.CardBody(html.Div(id='response-area'))
                ], className='mb-3'),
                color="#FFFFFF", type="dot", fullscreen=False,
            ),
        ], width=12)
    )
], fluid=True, className='py-3')
"""

"""
#[working] Final UI
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1('SSN Bot', className='text-center my-3 text-primary'), width=12)
    ),
    dbc.Row(
        dbc.Col(html.H3('Ask any question about getting your SSN', className='text-center text-secondary'), width=12)
    ),
    dbc.Row(
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Go ahead:', className='card-title', style={'fontWeight': 'bold'}),
                    dcc.Textarea(
                        id='question-area',
                        value='',
                        style={'width': '100%', 'height': '100px', 'resize': 'none', 'marginTop': '10px', 'borderRadius': '5px', 'border': '1px solid #ced4da'}
                    ),
                    html.Br(),
                    dbc.Button('Submit', id='submit-btn', color='primary', className='my-2', style={'width': '100%', 'padding': '10px 0', 'fontSize': '16px'}),
                ])
            ], className='my-3'),
            dcc.Loading(
                dbc.Card(id="load", children=[
                    dbc.CardBody(html.Div(id='response-area', style={'whiteSpace': 'pre-wrap', 'padding': '10px', 'border': '1px solid #ced4da', 'borderRadius': '5px', 'backgroundColor': '#f8f9fa'}))
                ], className='mb-3'),
                color="#007bff", type="dot", fullscreen=False,
            ),
        ], width=12)
    )
], fluid=True, className='py-3')
"""

"""
[working]
## next UI
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1('SSN Bot', className='text-center my-3', style={'fontFamily': 'Pacifico', 'color': '#007bff'}), width=12)
    ),
    dbc.Row(
        dbc.Col(html.H3('Ask any question about getting your SSN', className='text-center', style={'fontFamily': 'Roboto', 'color': '#6c757d'}), width=12)
    ),
    dbc.Row(
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Go ahead:', className='card-title', style={'fontWeight': 'bold', 'fontFamily': 'Roboto'}),
                    dcc.Textarea(
                        id='question-area',
                        value='',
                        style={'width': '100%', 'height': '100px', 'resize': 'none', 'marginTop': '10px', 'borderRadius': '5px', 'border': '1px solid #ced4da'}
                    ),
                    html.Br(),
                    dbc.Button([
                        html.Span('💬', style={'marginRight': '10px'}),
                        'Submit'
                    ], id='submit-btn', color='primary', className='my-2', style={'width': '100%', 'padding': '10px 0', 'fontSize': '16px'}),
                ])
            ], className='my-3'),
            dcc.Loading(
                dbc.Card(id="load", children=[
                    dbc.CardBody(html.Div(id='response-area', style={'whiteSpace': 'pre-wrap', 'padding': '10px', 'border': '1px solid #ced4da', 'borderRadius': '5px', 'backgroundColor': '#f8f9fa'}))
                ], className='mb-3'),
                color="#007bff", type="dot", fullscreen=False,
            ),
        ], width=12)
    )
], fluid=True, className='py-3', style={'fontFamily': 'Roboto'})

"""

## dark mode UI
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

dark_mode_styles = {
    'backgroundColor': '#1e1e1e',
    'color': '#f8f9fa',
    'borderColor': '#343a40',
}

app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H1('SSN Bot', className='text-center my-3', style={'fontFamily': 'Pacifico', 'color': '#007bff'}), width=12)
    ),
    dbc.Row(
        dbc.Col(html.H3('Ask any question about getting your SSN', className='text-center', style={'fontFamily': 'Roboto', 'color': '#f8f9fa'}), width=12)
    ),
    dbc.Row(
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Label('Go ahead:', className='card-title', style={'fontWeight': 'bold', 'fontFamily': 'Roboto', 'color': '#f8f9fa'}),
                    dcc.Textarea(
                        id='question-area',
                        value='',
                        style={'width': '100%', 'height': '100px', 'resize': 'none', 'marginTop': '10px', 'borderRadius': '5px', 'border': '1px solid #343a40', 'backgroundColor': '#343a40', 'color': '#f8f9fa'}
                    ),
                    html.Br(),
                    dbc.Button([
                        html.Span(className='fas fa-paper-plane', style={'marginRight': '10px'}),
                        'Submit'
                    ], id='submit-btn', color='primary', className='my-2', style={'width': '100%', 'padding': '10px 0', 'fontSize': '16px', 'transition': 'background-color 0.3s', 'borderRadius': '5px'}),
                ])
            ], className='my-3', style={'backgroundColor': '#2c2c2c', 'border': '1px solid #343a40', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}),
            dcc.Loading(
                dbc.Card(id="load", children=[
                    dbc.CardBody(html.Div(id='response-area', style={'whiteSpace': 'pre-wrap', 'padding': '10px', 'border': '1px solid #343a40', 'borderRadius': '5px', 'backgroundColor': '#2c2c2c', 'color': '#f8f9fa'}))
                ], className='mb-3', style={'backgroundColor': '#2c2c2c', 'border': '1px solid #343a40', 'boxShadow': '0 4px 8px rgba(0, 0, 0, 0.1)'}),
                color="#007bff", type="dot", fullscreen=False,
            ),
        ], width=12)
    )
], fluid=True, className='py-3', style={'backgroundColor': '#1e1e1e', 'fontFamily': 'Roboto'})


@callback(
    Output('response-area', 'children'),
    Input('submit-btn', 'n_clicks'),
    State('question-area', 'value'),
    prevent_initial_call=True
)
def create_response(_, question):
    answer = ai_bot.query(question)
    return answer


if __name__ == '__main__':
    app.run_server(debug=False)