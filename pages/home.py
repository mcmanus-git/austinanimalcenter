import dash
from dash import html, dcc, get_asset_url
import dash_bootstrap_components as dbc
from data_helpers import get_intake_outcomes_data
from graph_helpers import *

dash.register_page(
    __name__,
    name='AAC Insights',
    top_nav=True,
    path='/'
)

# Data
full_df = get_intake_outcomes_data()

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

explaination_paragrah = dcc.Markdown("""This dashboard was created with 
[Plotly Dash Open Source](https://dash.plotly.com/) over the course of 2 weeks between July 17 - July 31, 2022 and is part
 of Plotly's [Summer Community App Challenge](https://community.plotly.com/t/summer-community-app-challenge/65099). 
You can find out more on the [About Page](/about).  Get familiar with some of the amazing work Austin Animal Center 
has done below, check out the [Tools Page](/tools), and if you have a missing pet, check our [Missing Family Members
Map](/lost) to help you locate your missing loved one.

We plan to continue iterating, so have fun exploring and check back again soon!""")

icon_card = dbc.Card(
    dbc.CardBody(
        [
            html.I(className="fas fa-spinner fa-spin fa-2x"),
            html.I(className="fas fa-dog fa-2x"),
            html.I(className="fas fa-cat fa-2x"),
        ]
    )
)

tab1_content = html.Div(
    [html.Br(),
     dbc.Card(
         dbc.CardBody(
             [
                 html.Br(),
                 html.H4("Check out some dogs"),
                 dcc.Markdown("Some dog info I'm sure you're going to love)."
                              ),
                 # html.Br(),
                 # cards_row_1,
                 # html.Br(),
                 # cards_row_2,
                 # html.Br()
             ]
         )
     )
     ]
)

tab2_content = dbc.Card(
    dbc.CardBody(
        [
            # create_tab_resume()
            'Kitties stuff here'
        ]
    ),
    className="mt-3",
)

tab3_content = dbc.Card(
    dbc.CardBody(
        [
            html.H4("Birds"),
            dcc.Markdown("Some Bird Facts Here"),
        ]
    ),
    className="mt-3",
)

tabs = dbc.Tabs(
    [
        # dbc.Tab(tab1_content, label="Portfolio"),
        dbc.Tab(tab1_content, labelClassName="fas fa-dog fa-4x"),
        dbc.Tab(tab2_content, labelClassName="fas fa-cat fa-4x"),
        dbc.Tab(tab3_content, labelClassName="fas fa-spinner fa-spin fa-2x"),
    ]
)

version = html.P("""Version: 0.1.0  |  All Data current through July 17, 2022""", style={'fontSize': 10})


def layout():
    layout = html.Div([
        pet_image,
        pet_image_credit,
        html.Div(
            [
                header,
                html.Br(),
                html.Br(),
                explaination_paragrah,
                # icon_card,
                html.Br(),
                # tabs, # Could not complete in time for the Summer Challenge - Will complete afterward
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
