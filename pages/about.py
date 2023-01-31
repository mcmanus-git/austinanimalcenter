import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(
    __name__,
    name='About',
    top_nav=True,
    path='/about'
)

header = html.H1('About', style={'textAlign': 'center'})
line_break = html.Div([dcc.Markdown("""___""")], style={'margin': '5% 0% 5% 0%'})
explaination_paragrah = dcc.Markdown("""This dashboard was created with 
[Plotly Dash Open Source](https://dash.plotly.com/) and is part of Plotly's
[Summer Community App Challenge](https://community.plotly.com/t/summer-community-app-challenge/65099). 
As described by Adam at Plotly, """)

# Block Quotes Don't Render Properly - sigh
challenge_explanation_block = dcc.Markdown('''  
## "  
*We know people love building Dash apps.* 
We also know people strive to make this world a better place. 
So we thought, why not combine the two and make an exciting community app-building challenge?!

Plotly would like to challenge the community to build a Dash app that will support people working at animal shelters in 
understanding their data better and allow for higher rates of animal adoption.
[[1]](https://community.plotly.com/t/summer-community-app-challenge/65099)
## "''')

data_sources_header = html.H3('Data Sources', style={'textAlign': 'center'})
challenge_data_sources = dcc.Markdown('''  
Data sources used in this dashboard went above the requirements of the 
[Summer Community App Challenge](https://community.plotly.com/t/summer-community-app-challenge/65099) and used full 
datasets from [data.austintexas.gov](https://data.austintexas.gov/).    

- [Austin Animal Center Outcomes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Outcomes/9t4d-g238)  
Animal Center Outcomes from Oct, 1st 2013 to present. Outcomes represent the status of animals as they leave the Animal 
Center. All animals receive a unique Animal ID during intake. Annually over 90% of animals entering the center, are 
adopted, transferred to rescue or returned to their owners. The Outcomes data set reflects that Austin, TX. is the 
largest "No Kill" city in the country.  

- [Austin Animal Center Intakes](https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Intakes/wter-evkm)  
Animal Center Intakes from Oct, 1st 2013 to present. Intakes represent the status of animals as they arrive at the 
Animal Center. All animals receive a unique Animal ID during intake. Annually over 90% of animals entering the center, 
are adopted, transferred to rescue or returned to their owners.  

- [Austin Animal Center Stray Map API](https://dev.socrata.com/foundry/data.austintexas.gov/kz4x-q9k5)  
Map shows all stray cats and dogs that are currently listed in AAC's database for no longer than a week. 
Most will be located at AAC, but some will be held by citizens, which will be indicated on the "At AAC" column. 
Please [click here](checkhttp://www.austintexas.gov/department/lost-found-pet) for more information.
''')

creator_header = html.H1('About the Creator', style={'textAlign': 'center'})
contact_creator_header = html.H4('-   Contact Me   -', style={'textAlign': 'center'})
about_the_creator = dcc.Markdown("""Michael McManus is a Data Scientist who works for a regulated gas and electric 
utility in Michigan, U.S. His work focuses on electric grid reliability and resiliency as it relates to forestry 
related power outages. Michael graduated from the University of Michigan School of Information with a Master's Degree 
in Applied Data Science in May of 2022. Michael loves all things data and is constantly looking for new opportunities 
to do good with his Data Science skills and leave the world better than he found it.  

"Information Changes Everything" - UMSI.
""")


contact_links = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(dbc.NavLink([html.I(className="fab fa-github"), " GitHub"],
                                             href="https://github.com/mcmanus-git",
                                             target="_blank"))
                    ], width={"size": 3, 'offset': 2}
                ),
                dbc.Col(
                    [
                        html.Div(dbc.NavLink([html.I(className="fab fa-medium"), " Medium"],
                                             href="https://medium.com/@mcmanus_data_works",
                                             target="_blank")),
                    ], width={"size": 3}
                ),
                dbc.Col(
                    [
                        html.Div(dbc.NavLink([html.I(className="fab fa-linkedin"), " LinkedIn"],
                                             href="https://www.linkedin.com/in/michael-mcmanus/",
                                             target="_blank"))
                    ], width={"size": 3}
                )
            ], justify="center"
        )
    ]
)


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Br(),
                    explaination_paragrah,
                    html.Br(),
                    html.Div(
                        [
                            challenge_explanation_block
                        ], style={'margin': '0% 10% 10% 10%'}
                    ),
                    data_sources_header,
                    html.Br(),
                    challenge_data_sources,
                    html.Br(),
                    line_break,
                    creator_header,
                    html.Br(),
                    about_the_creator,
                    html.Br(),
                    html.Br(),
                    line_break,
                    html.Br(),
                    contact_creator_header,
                    html.Br(),
                    contact_links

                    # More Children
                ], style={'margin': '5% 10% 5% 10%'}
            )
        ]
    )
    return layout
