# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import base64
import math

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# load CA fires dataset
cal_fire = pd.read_csv('cal_fire.csv', low_memory=False)

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

# get list of counties and years
yr_options = cal_fire["FIRE_YEAR"].unique()
yr_options = [str(x) for x in yr_options]
yr_options.sort()
yr_options = ['All Years'] + yr_options
# yr_options.append('All Years')
county_options = cal_fire["FIPS_NAME"].unique()
county_options = [x for x in county_options if x==x]
# county_options = county_options.tolist()
county_options.sort()
county_options = ['All Counties'] + county_options
# county_options.append('All Counties')


# placeholder image
placeholder_img = base64.b64encode(open('test_img.png', 'rb').read())
# kepler map html
kep_viz = html.Iframe(srcDoc = open('kepler.gl_1yr.html').read(), height='500', width='100%')

app_color = {"graph_bg": "#082255", "graph_line": "#007ACE"}

app.layout = html.Div(children=[
            # heading div tag - title and description
            html.Div(
            [
                dbc.Card(
                    dbc.CardBody([
                        html.H2(children='California Wildfires Dashboard'),

                        html.Div(children='''
                            The goal of this dashboard is to visualize the historic wildfires in California, ranging from 1992-2015.
                            The hope is that this visualization will allow the state of California to explore interesting patterns
                            in the data and identify where additional resources may be needed to alleviate impact in the future.
                        ''')
                    ])
                )
            ],
            ),
            html.Div([
                html.Div([
                    dbc.Card(
                        dbc.CardBody([
                            html.Div([
                                #html.Img(src='data:image/png;base64,{}'.format(placeholder_img.decode()), style={'height':'100%', 'width':'80%'})
                                kep_viz
                            ],style={'height':'100%', 'textAlign': 'center'}),
                        ]),
                    ),
                ]),

            ]),

            # content div tag
            html.Div([
            dbc.Card(
                dbc.Row([
                    # drop downs
                    dbc.Col(
                        dbc.CardBody([
                            dcc.Dropdown(
                                id="Year",
                                options=[{
                                    'label': i,
                                    'value': i
                                } for i in yr_options],
                                value='All Years',
                                style={'backgroundColor': '#2f363d'},
                                placeholder="Select a year"),

                        ]),
                    width=6, style={"height": "100%"}),
                    dbc.Col(
                        dbc.CardBody([
                                dcc.Dropdown(
                                id="County",
                                options=[{
                                    'label': i,
                                    'value': i
                                } for i in county_options],
                                value='All Counties',
                                style={'backgroundColor': '#2f363d'},
                                placeholder="Select a county"),
                        ]),
                    width=6, style={"height": "100%"})
                ],no_gutters=True),),
                # plots div tag
                html.Div([
                    dbc.Row([
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody([
                                    dcc.Graph(id='cal_cause')
                                ])
                            )
                        ),
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody([
                                    dcc.Graph(id='cal_size')
                                ])
                            )
                        )
                    ],no_gutters=True)

                ],),
            ])
])

# make updates
@app.callback(
    [Output('cal_cause', 'figure'), Output('cal_size', 'figure')],
    [Input('Year', 'value'),
     Input('County', 'value')])

def update_graph(year_val, county_val):
    if year_val is None or year_val == '':
        year_val = 'All Years'
    if county_val is None or county_val == '':
        county_val = 'All Counties'

    if year_val == 'All Years':
        df_plot = cal_fire.copy()
    else:
        df_plot = cal_fire[cal_fire["FIRE_YEAR"]== int(year_val)]

    if county_val != 'All Counties':
        df_plot =  df_plot[df_plot["FIPS_NAME"]== county_val]

    # group by cause
    cause_plot = df_plot.groupby('STAT_CAUSE_DESCR')['OBJECTID'].count().reset_index(name='count')
    # bar plot by cause
    fig = go.Figure(go.Bar(
                y=cause_plot['STAT_CAUSE_DESCR'],
                x=cause_plot['count'], text=cause_plot['count'],textposition='auto',
                orientation='h'), layout=dict(template='plotly_dark'))
    fig.update_layout(title='California Wildfire Causes', xaxis_title="Frequency",
        yaxis_title="Cause", yaxis={'categoryorder':'total ascending'})

    # histogram frequency of fire size
    if not df_plot.empty:
        fig2 = px.histogram(x=np.log(df_plot["FIRE_SIZE"])+1, nbins=50, template='plotly_dark')
        fig2.update_layout(title='Log Distribution of CA Fire Size (Acres)', xaxis_title="log(Fire Size)",
            yaxis_title="Frequency")
    else:
        fig2 = {}

    return fig, fig2



if __name__ == '__main__':
    app.run_server(debug=True)
