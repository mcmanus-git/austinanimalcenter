from dash import html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from page_home import create_page_home
from page_lost_animals import create_page_lost_animals
from page_tools import create_page_tools
from page_about import create_page_about
from app import app
sample_var = 'nothing'

server = app.server
app.config.suppress_callback_exceptions = True

app.layout = dbc.Container(html.Div([
    dcc.Location(id='url', refresh=False),
    dcc.Loading(id="loading_page_content",
                children=[
                    html.Div(id='page-content')],
                # type="cube",
                color='#000000',
                fullscreen=True
                ),

]), fluid=True, className="dbc", style={'padding': 0})


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/lost':
        return create_page_lost_animals()
    if pathname == '/tools':
        return create_page_tools()
    if pathname == '/about':
        return create_page_about()
    else:
        return create_page_home()


if __name__ == '__main__':
    app.run_server(debug=False)
