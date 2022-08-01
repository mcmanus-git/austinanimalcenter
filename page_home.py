from dash import html, dcc
import dash_bootstrap_components as dbc
from navbar import create_navbar
from data_helpers import get_intake_outcomes_data
from graph_helpers import *
from app import app
sample_var = 'nothing'
nav = create_navbar()

# Data
full_df = get_intake_outcomes_data()

# Graphs
intake_animal_type_count_hbar = create_intake_animal_type_count_hbar(full_df, aac_color('blue'))
intake_over_time = create_intake_over_time(full_df)
outcomes_by_type = create_graph_outcomes(full_df, aac_color('blue'))

# Images
pet_image = html.Div(html.Img(src=app.get_asset_url('silvana-carlos-TPdR4J19SGQ-unsplash.jpg'), style={'width': '100%'}))
pet_image_credit = html.A("  Photo: Silvana Carlos via Unsplash",
                          href='https://unsplash.com/photos/TPdR4J19SGQ',
                          target="_blank",
                          style={'fontSize': 10}
                          )

header = html.H3('Austin Animal Center - Data Insights',
                 style={'textAlign': 'center'}
                 )

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


def create_page_home():
    layout = html.Div([
        nav,
        pet_image,
        pet_image_credit,
        html.Div(
            [
                header,
                html.Br(),
                html.Br(),
                # icon_card,
                html.Br(),
                tabs,
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
            ], style={'margin': '5% 5% 5% 5%'}
        )
    ])
    return layout
