import os
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from data_helpers import get_stray_df
import folium
from datetime import datetime

sample_var = 'nothing'


def aac_color(color_string):
    aac_color_dict = {'green': '#3AB02C',
                      'red': '#D23137',
                      'yellow': '#FFA708',
                      'orange': '#F89521',
                      'purple': '#211552',
                      'blue': '#187FA3',
                      'black': '#1E1E1E'
                      }

    return aac_color_dict[color_string.lower()]


def create_intake_animal_type_count_hbar(df, aac_color):
    intake = df[df['Transaction Type'] == 'Intake'].copy()
    earliest_year = intake['DateTime'].dt.year.min()
    fig = px.bar(intake['Animal Type'].value_counts().reset_index().sort_values('Animal Type', ascending=True),
                 x='Animal Type',
                 y='index',
                 template='plotly_white',
                 orientation='h',
                 labels={'Animal Type': 'Number of Animals', 'index': ''},

                 )

    fig.update_traces(marker_color=aac_color)
    fig.update_layout(title_text=f'Number of Animals Given Shelter Since {earliest_year}', title_x=0.5)
    return fig


def create_intake_over_time(df):
    intake = df[df['Transaction Type'] == 'Intake'].copy()
    fig = px.line(intake.groupby([pd.to_datetime(intake['DateTime'].dt.strftime('%B %Y')), 'Animal Type']).size().reset_index().sort_values('DateTime', ascending=True).rename({0: 'Number of Animals', 'DateTime': 'Date'}, axis=1), x='Date', y='Number of Animals', color='Animal Type', template='plotly_white', hover_data={"Date": "|%B %d, %Y"})
    fig.update_layout(title_text=f'Animals Given Shelter Over Time', title_x=0.5, yaxis_title=None, xaxis_title=None)
    fig.update_xaxes(
        dtick="M3",
        tickformat="%b\n%Y",
        ticklabelmode='period',
        tickangle=0
    )
    return fig


def create_graph_outcomes(df, aac_color):

    ts = df[df['Transaction Type'] == 'Outcome']\
        .groupby(['Outcome Type', 'Outcome Subtype'])\
        .size()\
        .reset_index()\
        .rename({0: 'Number of Animals'}, axis=1)[['Outcome Type', 'Outcome Subtype', 'Number of Animals']]

    fig = go.Figure(data=[
        go.Bar(name='Type', x=[tuple(ts['Outcome Type']), tuple(ts['Outcome Subtype'])],
               y=list(ts['Number of Animals'])),
    ])

    fig.update_traces(marker_color=aac_color)
    # Change the bar mode
    fig.update_layout(barmode='group', template='plotly_white', title_text=f'Animal Outcomes', title_x=0.5)
    return fig


def create_lost_animal_map():
    stray_df = get_stray_df()
    records = stray_df.dropna()[['latitude',
                                 'longitude',
                                 'image_url',
                                 'animal_id',
                                 'intake_date',
                                 'type',
                                 'looks_like',
                                 'color',
                                 'sex']
    ].to_records()

    austin_map = folium.Map(location=[30.2672, -97.7431], zoom_start=10)
    # Add the marker to the map...
    # folium.Marker(location=[37.0902, -95.7129]).add_to(kansas_map)
    # Display the map with the marker that's been added

    for record in records:

        img_src_url = f"http://petharbor.com/get_image.asp?RES=Detail&ID={record[4]}&LOCATION=ASTN"
        html = f'<html><body><img src="{img_src_url}" width="128"><br><br>Contact AAC<br><a aria-label="512-974-2000" href="tel:512-974-2000">512-974-2000</a><br></body></html>'
        popup = folium.Popup(folium.Html(html, script=True))

        tooltip = (
            "<b>Date Found:</b> {}<br>"
            "<b>Animal Type:</b> {}<br>"
            "<b>Description: </b>{} {} {}<br>"
            "<br><b>Click for Photo</b><br>"
        ).format(record[5],
                 record[6],
                 record[8],
                 record[9],
                 record[7]
                 )

        # Records Note:
        # 1 'latitude',
        # 2 'longitude',
        # 3 'image_url',
        # 4 'animal_id',
        # 5 'intake_date',
        # 6 'type',
        # 7 'looks_like',
        # 8 'color',
        # 9 'sex'

        folium.Marker(location=[record[1], record[2]],
                      icon=folium.Icon(#color=color_dict[record[3]],
                          icon_color='white',
                          icon='paw',
                          prefix='fa',
                      ),
                      popup=popup,
                      tooltip=tooltip
                      ).add_to(austin_map)

    austin_map.save(f'data/assets/stray_map_{datetime.now().strftime("%m_%d_%Y")}.html')

    return austin_map


def get_stray_map():

    files = os.listdir(f'data/full/')
    if len(files) > 0:
        for file in files:
            if 'stray_map' in file:
                file_name = file
            else:
                file_name = None
    else:
        file_name = None

    if file_name and file_name[-15:-5] == f'{datetime.now().strftime("%m_%d_%Y")}':
        stray_df = pd.read_pickle(f"data/full/{file_name}")
    else:
        stray_df = create_lost_animal_map()

    stray_map_string = f'data/assets/stray_map_{datetime.now().strftime("%m_%d_%Y")}.html'

    return stray_map_string
