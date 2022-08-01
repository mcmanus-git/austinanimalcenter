import pandas as pd
import os
from sodapy import Socrata
import json
from datetime import datetime

sample_var = 'nothing'
def get_intake_outcomes_data():
    df = pd.read_pickle(f'data/full/aac_data_clean_2022_7_17.pkl')
    return df


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


def get_stray_df():

    files = os.listdir(f'data/full/')
    if len(files) > 0:
        for file in files:
            if 'aac_stray_' in file:
                file_name = file
            else:
                file_name = None
    else:
        file_name = None

    if file_name and file_name[-14:-4] == f'{datetime.now().strftime("%m_%d_%Y")}':
        stray_df = pd.read_pickle(f"data/full/{file_name}")
    else:
        stray_df = update_stray_data()

    return stray_df
