import dash
from dash import html, dcc, get_asset_url
import dash_bootstrap_components as dbc
from navbar import create_navbar

# Toggle the themes at [dbc.themes.LUX]
# The full list of available themes is:
# BOOTSTRAP, CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE,
# SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI, ZEPHYR.
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/

navbar = create_navbar()
FA512 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"

# For meta tags
app_description = """
Machine Learning, Data Exploration, and
Analytics Web Application showcasing that leveraging data supports
Austin Animal Center's operational efficiency and increase animal
adoption rates.
"""
app_title = "Austin Animal Center Insights"
app_image = 'https://unsplash.com/photos/TPdR4J19SGQ'

metas = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    {"property": "twitter:card", "content": "summary_large_image"},
    {"property": "twitter:url", "content": "https://www.wealthdashboard.app/"},
    {"property": "twitter:title", "content": app_title},
    {"property": "twitter:description", "content": app_description},
    {"property": "twitter:image", "content": app_image},
    {"property": "og:title", "content": app_title},
    {"property": "og:type", "content": "website"},
    {"property": "og:description", "content": app_description},
    {"property": "og:image", "content": app_image},
]

app = dash.Dash(__name__,
                suppress_callback_exceptions=True,
                external_stylesheets=[dbc.themes.LUX,
                                      FA512,
                                      ],
                title='AAC Insights',
                use_pages=True,
                meta_tags=metas #[
                #     {
                #         "name": "viewport",
                #         "content": "width=device-width, initial-scale=1"
                #     }
                # ],
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
    app.run_server(debug=False)
