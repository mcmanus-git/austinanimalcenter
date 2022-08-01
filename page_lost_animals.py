from dash import html, dcc
from navbar import create_navbar
from graph_helpers import get_stray_map
from datetime import datetime
sample_var = 'nothing'
nav = create_navbar()

header = html.H3('Lost and Found Family Members', style={'textAlign': 'center'})
explanation_paragraph = html.Div(
    [
        dcc.Markdown("""### Missing a family member  
We know it's hard to lose a loved one. Check the map above and see whether we were able to locate your
missing family member. Hover above the markers on the map to get more information about the animals we've found. 
Click the marker to view a picture of the animal where available. If you see your animal, contact Austin Animal Center 
at 512-974-2000 and we'll help you reconnect with your loved one.""")
    ]
)


def create_page_lost_animals():

    layout = html.Div(
        [
            nav,
            html.Div(
                [
                    header,
                    html.Br(),
                    html.Iframe(id='stray_map',
                                srcDoc=open(get_stray_map(), 'r').read(),
                                width='100%',
                                height='500'
                                ),
                    html.P(f"Data Updated {datetime.now().strftime('%B %d, %Y')}", style={'fontSize': 10}),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    explanation_paragraph,
                ], style={'margin': '5% 5% 5% 5%'}
            )
        ]
    )
    return layout
