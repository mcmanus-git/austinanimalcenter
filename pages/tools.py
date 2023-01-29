import dash
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import pickle
from dateutil.relativedelta import relativedelta
from datetime import datetime
import pandas as pd
import numpy as np
from catboost import CatBoostRegressor

dash.register_page(
    __name__,
    name='Tools',
    top_nav=True,
    path='/tools'
)

with open('regressor/model_inputs_dict.pkl', 'rb') as pkl:
    dropdown_vals_dict = pickle.load(pkl)

reg = CatBoostRegressor()
reg.load_model('regressor/animal_stay_reg_v1.cbm')

header = html.H1('Tools', style={'textAlign': 'center'})
line_break = html.Div([dcc.Markdown("""___""")], style={'margin': '5% 0% 5% 0%'})
explaination_paragrah = dcc.Markdown("""In an endeavor to come up with tools which put data to good use, 
we utilize Machine Learning to help Austin Animal Center predict the 
length of stay of newly sheltered animals.  Using historical data, a Machine Learning Model was trained
to predict new animals' length of stay and care with AAC which will help the center better predict costs.""")

animal_stay_calculator = dcc.Markdown("""### Animal Stay Estimator  
This tool provides an estimated length of care an incoming animal is likely to need. To use the tool, fill in the 
information of the incoming animal, and we'll provide an estimated care length. Our hope is that this tool will enable 
staff to better predict cost and capacity of the Austin Animal Center""")

animal_likely_outcome = dcc.Markdown("""### Most Likely Outcome  
As the [Plotly Dash Summer Community App Challenge](https://community.plotly.com/t/summer-community-app-challenge/65099)
 ran from July 15, 2022 - July 31, 2022, the time constraint made it impossible to complete this tool
by the deadline. The creator has every intention of completing and improving this tool iteratively. 
The primary purpose of this tool is to use Machine Learning to predict the most likely outcome of incoming 
animals to help prepare Austin Animal Center for capacity and supply chain needs such as food, medication, and health 
care for the animal.""")

disclaimer = html.P("""Note: If the animal is less than 1 year old, select 1. 
Be advised, the accuracy of this model varies by breed and animal type.""", style={'fontSize': 10})

stay_calculator_inputs = html.Div(
    [
        html.Div(
            [
                html.Div( # Animal Type
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['Animal Type'],
                            id='animal_type_input',
                            placeholder='Animal Type',
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                html.Div( # Color
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['Color'],
                            id='animal_color_input',
                            placeholder='Color',
                            searchable=True
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                html.Div( # Sex
                    [
                        dcc.Dropdown(
                            ['Male', 'Female'],
                            id='animal_sex_input',
                            placeholder='Sex',
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                html.Div( # Reproductive Status
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['Reproductive Status'],
                            id='animal_reproductive_status_input',
                            placeholder='Reproductive Status'
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '25%'
                    }
                ),
                html.Div( # Intake Condition
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['Intake Condition'],
                            id='animal_intake_condition_input',
                            placeholder='Intake Condition'
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '25%'
                    }
                ),
                html.Div( # Years Old
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['transaction_age_years'],
                            id='animal_years_old_input',
                            placeholder='Years Old',
                            searchable=True,
                        ),
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                html.Div( # Breed
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['Breed'],
                            id='animal_breed_input',
                            placeholder='Breed',
                            searchable=True,
                            optionHeight=75
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                html.Div( # Intake Type
                    [
                        dcc.Dropdown(
                            dropdown_vals_dict['Intake Type'],
                            id='animal_intake_type_input',
                            placeholder='Intake Type',
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                html.Div( # Multiple Intakes
                    [
                        dcc.Dropdown(
                            ['Yes', 'No'],
                            id='animal_multiple_intakes_input',
                            placeholder='Multiple Intakes',
                        )
                    ], style={
                        'display': 'inline-block',
                        'vertical-align': 'middle',
                        'margin': '1% 1% 1% 1%',
                        'width': '20%'
                    }
                ),
                # dcc.Dropdown
            ], style={
                'display': 'inline-block',
                'vertical-align': 'middle',
                'margin': '0% 1% 0% 1%',
                'width': '100%'
            }
        )
    ]
)


stay_prediction_output_div = html.Div(
    id='animal_stay_pred_output'
)

version = html.P("""Version: 0.1.0  |  All Data current through July 17, 2022""", style={'fontSize': 10})


def layout():
    layout = html.Div(
        [
            html.Div(
                [
                    header,
                    html.Br(),
                    explaination_paragrah,
                    html.Br(),
                    line_break,
                    html.Br(),
                    animal_stay_calculator,
                    html.Br(),
                    disclaimer,
                    html.Br(),
                    stay_calculator_inputs,
                    html.Br(),
                    html.Br(),
                    stay_prediction_output_div,
                    html.Br(),
                    html.Br(),
                    line_break,
                    html.Br(),
                    animal_likely_outcome,
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    version,
                    # More Children
                ], style={'margin': '5% 10% 5% 10%'}
            )
        ]
    )
    return layout


@callback(
    Output('animal_stay_pred_output', 'children'),
    Input('animal_type_input', 'value'),
    Input('animal_color_input', 'value'),
    Input('animal_sex_input', 'value'),
    Input('animal_reproductive_status_input', 'value'),
    Input('animal_intake_condition_input', 'value'),
    Input('animal_years_old_input', 'value'),
    Input('animal_breed_input', 'value'),
    Input('animal_intake_type_input', 'value'),
    Input('animal_multiple_intakes_input', 'value'),
)
def update_stay_pred(type, color, sex, status, condition, years_old, breed, intake_type, multiple_intakes):
    print(type, color, sex, status, condition, years_old, breed, intake_type, multiple_intakes)
    if years_old:
        if years_old < 1:
            years_old = 1
        dob = datetime.now() - relativedelta(years=years_old)
        f_date = dob
        l_date = datetime.now()
        age_days = (l_date - f_date).days
        age_days

    if multiple_intakes == 'Yes':
        multiple_intakes = True
    elif multiple_intakes == 'No':
        multiple_intakes = False
    if multiple_intakes != None and all([type, color, sex, status, condition, years_old, breed, intake_type]):
        pred_inputs = {'Animal Type': type, 'Breed': breed, 'Color': color, 'Date of Birth': dob,
                       'Multiple Intakes': multiple_intakes, 'DateTime': datetime.now(),
                       'transaction_age_years': years_old, 'Intake Type': intake_type, 'Intake Condition': condition,
                       'Reproductive Status': status, 'Sex': sex, 'Age at Transaction': age_days,
                       }

        predicted_stay = reg.predict(pd.DataFrame(pred_inputs, index=[0]))

        pred_string = f"Predicted Length of Care in Days: {int(np.ceil(predicted_stay[0]))}"

    elif not all([type, color, sex, status, condition, years_old, breed, intake_type, multiple_intakes]):
        pred_string = """Please enter all information about the incoming animal and a predicted length of care will be 
        provided."""

    return pred_string
