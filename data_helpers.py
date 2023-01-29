import pandas as pd
import os
from sodapy import Socrata
import json
from datetime import datetime
from dateutil import relativedelta
import urllib.request
import numpy as np
import calendar


def intck_month(start, end):
    rd = relativedelta.relativedelta(pd.to_datetime(end), pd.to_datetime(start))
    return {
        'transaction_age_years': rd.years,
        'transaction_age_months': rd.months,
        'transaction_age_weeks': rd.weeks,
        'transaction_age_days': rd.days
    }


def clean_outcome_intake_data(out_df, in_df):

    intake_keep_cols = [
        'Animal ID', 'Name', 'DateTime', 'Found Location', 'Intake Type', 'Intake Condition', 'Animal Type',
        'Sex upon Intake', 'Age upon Intake', 'Breed', 'Color', 'Transaction Type'
    ]
    outcome_keep_cols = [
        'Animal ID', 'Name', 'DateTime', 'Date of Birth', 'Outcome Type', 'Outcome Subtype', 'Animal Type',
        'Sex upon Outcome', 'Age upon Outcome', 'Breed', 'Color', 'Transaction Type'
    ]

    df = pd.concat([in_df[intake_keep_cols], out_df[outcome_keep_cols]]).sort_values(['Animal ID', 'DateTime']).reset_index(drop=True)
    df['Date of Birth'] = pd.to_datetime(df['Date of Birth'])
    df['Date of Birth'] = df[['Animal ID', 'Name']].merge(df[['Animal ID', 'Date of Birth']].groupby('Animal ID').max().reset_index(), on='Animal ID', how='left')['Date of Birth']
    df['Multiple Intakes'] = np.where(df['Animal ID'].isin((df[df['Transaction Type'] == 'Intake'].groupby('Animal ID').size() > 1).replace(False, np.nan).dropna().index), True, False)

    df[['transaction_age_years', 'transaction_age_months', 'transaction_age_weeks', 'transaction_age_days']] = df.apply(lambda x: intck_month(x['Date of Birth'], x['DateTime']) if not pd.isna(x['Date of Birth']) else {'transaction_age_years': None, 'transaction_age_months': None, 'transaction_age_weeks': None, 'transaction_age_days': None}, axis=1).apply(pd.Series)
    df['transaction_age_days'] = df['transaction_age_days'] - (df['transaction_age_weeks'] * 7)

    col_order = ['Animal ID',
                 'Animal Type',
                 'Name',
                 'Breed',
                 'Color',
                 'Date of Birth',
                 'Multiple Intakes',
                 'DateTime',
                 'Transaction Type',
                 'transaction_age_years',
                 'transaction_age_months',
                 'transaction_age_weeks',
                 'transaction_age_days',
                 'Found Location',
                 'Intake Type',
                 'Intake Condition',
                 'Sex upon Intake',
                 'Outcome Type',
                 'Outcome Subtype',
                 'Sex upon Outcome']

    df = df[col_order].reset_index(drop=True)

    return df


def get_updated_data():

    outcome_url = "https://data.austintexas.gov/api/views/9t4d-g238/rows.csv?accessType=DOWNLOAD"
    intakes_url = "https://data.austintexas.gov/api/views/wter-evkm/rows.csv?accessType=DOWNLOAD"
    filepath = 'data/full/'
    outcome_file = f"{filepath}Austin_Animal_Center_Outcomes_{datetime.now().strftime('%m_%d_%Y')}.csv"
    intake_file = f"{filepath}Austin_Animal_Center_Intakes_{datetime.now().strftime('%m_%d_%Y')}.csv"

    urllib.request.urlretrieve(outcome_url, outcome_file)
    urllib.request.urlretrieve(intakes_url, intake_file)

    outcomes = pd.read_csv(outcome_file)
    outcomes['DateTime'] = pd.to_datetime(outcomes['DateTime'])
    outcomes['Transaction Type'] = 'Outcome'

    intakes = pd.read_csv(intake_file)
    intakes['DateTime'] = pd.to_datetime(intakes['DateTime'])
    intakes['Transaction Type'] = 'Intake'

    df = clean_outcome_intake_data(outcomes, intakes)

    return df


def get_intake_outcomes_data():
    files = os.listdir(f'data/full/')

    current_year = datetime.now().year
    current_quarter = (datetime.now().month - 1) // 3 + 1

    filepath = 'data/full/'
    current_filename = f'{filepath}aac_data_clean_{current_year}_{current_quarter}.pkl'
    outcome_file = f"{filepath}Austin_Animal_Center_Outcomes_{datetime.now().strftime('%m_%d_%Y')}.csv"
    intake_file = f"{filepath}Austin_Animal_Center_Intakes_{datetime.now().strftime('%m_%d_%Y')}.csv"

    if current_filename.split('/')[-1] not in files:
        df = get_updated_data()
        df.to_pickle(current_filename)
        cleanup_stray_data('aac_data_clean_', filepath, files, current_filename)
        cleanup_stray_data('Austin_Animal_Center_Outcomes_', filepath, files, outcome_file)
        cleanup_stray_data('Austin_Animal_Center_Intakes_', filepath, files, intake_file)

    else:
        df = pd.read_pickle(current_filename)

    return df


def get_data_refresh_date():
    files = os.listdir('data/full')
    for file in files:
        if 'Austin_Animal_Center_Intakes_' in file:
            data_refresh_date = file.split('_')[-3:]
            data_refresh_date = f"{calendar.month_name[int(data_refresh_date[0])]} {data_refresh_date[1]}, {data_refresh_date[2].split('.')[0]}"

    return data_refresh_date


def update_stray_data():

    stray_map = 'kz4x-q9k5'
    client = Socrata("data.austintexas.gov", None)
    results = client.get(stray_map, limit=2000)

    # Convert to pandas DataFrame
    stray_df = pd.DataFrame.from_records(results)
    stray_df['image_url'] = stray_df['image'].apply(pd.Series)
    stray_df.drop('image', axis=1, inplace=True)
    stray_df['intake_date'] = pd.to_datetime(stray_df['intake_date'])

    loc_df = pd.DataFrame.from_dict(stray_df['location'].to_dict()).T
    loc_df = pd.concat([pd.DataFrame(loc_df['human_address'].apply(json.loads).to_dict()).T, loc_df[['latitude', 'longitude']]], axis=1)

    stray_df = pd.concat([stray_df[['animal_id', 'at_aac', 'intake_date', 'type', 'looks_like', 'color', 'sex', 'age', 'image_url']], loc_df], axis=1)
    stray_df['intake_date'] = stray_df['intake_date'].dt.strftime('%B %d, %Y')

    stray_df.to_pickle(f'data/full/aac_stray_{datetime.now().strftime("%m_%d_%Y")}.pkl')

    return stray_df


def cleanup_stray_data(file_prefix, file_path,  file_list, current_file_name):
    for file in file_list:
        if file_prefix in file and file != current_file_name.split('/')[-1]:
            os.remove(f'{file_path}{file}')


def get_stray_df():

    current_filename = f'data/full/aac_stray_{datetime.now().strftime("%m_%d_%Y")}.pkl'
    files = os.listdir(f'data/full/')

    if len(files) > 0:
        if current_filename in files:
            stray_df = pd.read_pickle(f"data/full/{current_filename}")
        else:
            stray_df = update_stray_data()
            cleanup_stray_data('aac_stray_', 'data/full/', files, current_filename)

    return stray_df
