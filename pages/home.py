import dash
from dash import html, dcc, get_asset_url
from data_helpers import get_intake_outcomes_data, get_data_refresh_date
from graph_helpers import *

dash.register_page(
    __name__,
    name='AAC Insights',
    path='/',
    title="AAC Insights",
    # image='silvana-carlos-TPdR4J19SGQ-unsplash.jpg',
    description="Austin Animal Center Data Exploration Web App.",
)

# Data
full_df = get_intake_outcomes_data()
data_refresh_date = get_data_refresh_date()

# Graphs
intake_animal_type_count_hbar = create_intake_animal_type_count_hbar(full_df, aac_color('blue'))
intake_over_time = create_intake_over_time(full_df)
outcomes_by_type = create_graph_outcomes(full_df, aac_color('blue'))

# Images
pet_image = html.Div(html.Img(src=get_asset_url('silvana-carlos-TPdR4J19SGQ-unsplash.jpg'), style={'width': '100%'}))
pet_image_credit = html.A("  Photo: Silvana Carlos via Unsplash",
                          href='https://unsplash.com/photos/TPdR4J19SGQ',
                          target="_blank",
                          style={'fontSize': 10}
                          )

header = html.H2('Austin Animal Center',
                 style={'textAlign': 'center'}
                 )

explanation_paragraph = dcc.Markdown("""This dashboard was created with 
[Plotly Dash Open Source](https://dash.plotly.com/) over the course of 2 weeks between July 17 - July 31, 2022 and is part
 of Plotly's [Summer Community App Challenge](https://community.plotly.com/t/summer-community-app-challenge/65099). 
You can find out more on the [About Page](/about).  Get familiar with some of the amazing work Austin Animal Center 
has done below, check out the [Tools Page](/tools), and if you have a missing pet, check our [Missing Family Members
Map](/lost) to help you locate your missing loved one.

We plan to continue iterating, so have fun exploring and check back again soon!""")


version = html.P(
    f"""Version: 0.1.9  |  All Data Current Through {data_refresh_date} Updated Quarterly""",
    style={'fontSize': 10}
)


def layout():
    layout = html.Div([
        pet_image,
        pet_image_credit,
        html.Div(
            [
                header,
                html.Br(),
                html.Br(),
                explanation_paragraph,
                html.Br(),
                html.Br(),
                html.Br(),
                dcc.Graph(figure=intake_animal_type_count_hbar),
                html.Br(),
                html.Br(),
                dcc.Graph(figure=intake_over_time),
                html.Br(),
                html.Br(),
                dcc.Graph(figure=outcomes_by_type),
                html.Br(),
                html.Br(),
                html.Br(),
                version,
            ], style={'margin': '5% 5% 5% 5%'}
        )
    ])
    return layout
