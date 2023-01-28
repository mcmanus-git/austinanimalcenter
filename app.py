import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# BOOTSTRAP, CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI, ZEPHYR.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

navbar = create_navbar()
FA47 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'
FA43 = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.3.0/css/font-awesome.min.css'
FA512 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.LUX,
                                      # FA47,
                                      # FA43,
                                      FA512,
                                      ],
                title='AAC Insights',
                use_pages=True,
                )


app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>AAC Insights</title>
        {%favicon%}
        {%css%}
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
        
    </body>
</html>
'''

app.layout = dcc.Loading(
    id='loading_page_content',
    children=[
        html.Div(
            [
                navbar,
                dash.page_container
            ]
        )
    ],
    color='#000000',
    fullscreen=True
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
