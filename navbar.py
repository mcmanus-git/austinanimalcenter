import dash_bootstrap_components as dbc

sample_var = 'nothing'
def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",
                align_end=True,
                children=[
                    dbc.DropdownMenuItem("Home", href='/'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("Lost Family Members", href='/lost'),
                    dbc.DropdownMenuItem("Tools", href='/tools'),
                    dbc.DropdownMenuItem("About", href='/about'),
                ],
            ),
        ],
        brand='Austin Animal Center',
        brand_href="/",
        sticky="top",
        color="primary",  # Change this to change color of the navbar e.g. "primary", "secondary" etc.
        dark=True,  # Change this to change color of text within the navbar (False for dark text)
    )

    return navbar
