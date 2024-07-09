import dash
from dash import Dash, html, dcc
import plotly.express as px # for bar chart
from dash.dependencies import Input, Output
import pandas as pd

from Components.apple_loader import load_apple_data
from Components.strava_loader import (
    load_strava_data,
    DataSchema,
)
from Components import (
    days_dropdown,
    dist_dow_bar,
    run_type_pie,
    run_dist_dropdown,
    run_type_dropdown,
    avg_pace_line,
    max_hr_line,
    vo2_max_line,
    training_hrs_bar,
    ids,
)

from flask import Flask
# app = dash.Dash(__name__)
# server = app.server

server = Flask(__name__)
app = dash.Dash(__name__, server=server)
server._got_first_request = server.before_first_request

STRAVA_DATA = "Data/activities.csv"
APPLE_DATA = "Data/VO2Max.csv"
strava_data = load_strava_data(STRAVA_DATA)
apple_data = load_apple_data(APPLE_DATA)

# -------------------------------------------------------------------------

def build_banner():
    return html.Div(
        id="banner",
        className="banner",
        children=[
            html.Div(
                id="banner-text",
                children=[
                    html.H1("Running Dashboard"),
                    html.H6("Created by Lorraine Sanares"),
                ],
            ),

        ],
        
    )
    
# -------------------------------------------------------------------------
    
def build_tabs():
    return html.Div(
        id="tabs",
        className="tabs",
        children=[
            dcc.Tabs(
                id="app-tabs",
                value="tab2",
                className="custom-tabs",
                children=[
                    dcc.Tab(
                        id="Specs-tab",
                        label="Running Stats",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Race Performance Predictor",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )

def generate_section_banner(title):
    return html.Div(className="section-banner", children=title)

# -------------------------------------------------------------------------


def build_top_panel():
    return html.Div(
        id="top-section-container",
        className="row",
        children=[

            html.Div(
                
                # BUILDING THE DROPDOWN PANNELS
                id="dropdown-section-container",
                style={"padding": "20px", "width": '26%'},
                children=[
                    generate_section_banner("Filters"),
                    html.H6('Day of Week'),
                    days_dropdown.render(app, strava_data),
                    html.H6('Distance'),
                    run_dist_dropdown.render(app, strava_data),
                    html.H6('Run Type'),
                    run_type_dropdown.render(app, strava_data),
                ],
                
            ),
            
            # HEATMAP IMAGE
            
            html.Div(
                id="stats-summary-session",
                className="row",
                style={"width": '47%'},
                children=[
                    generate_section_banner("Route Heatmap"),
                    html.Div(
                            html.Img(src='assets/heatmap_blue.jpg',
                            style={
                                "width": "100%",  # Specify the width
                                "height": "100%",  # Specify the height
                                # "padding": "10px",
                                # "border-bottom": "#1E2130 solid 0.8rem;"
                                },
                            ),
                    ),
                    generate_section_banner("Totals"),
                    html.Div(
                        id="top-row-graphs",
                        className="row container_display",
                        children=[
                            html.Div(
                                id="activities",
                                className="mini_container",
                                children=[
                                    html.P("Activities"),
                                    # summary_text.activity_text(app, strava_data)
                                    html.H6(str(len(strava_data)))
                                ]
                            ),
                            html.Div(
                                id="distance",
                                className="mini_container",
                                children=[
                                    html.P("Distance"),
                                    html.H6(f"{sum(strava_data['Distance'])} km")
                                ]     
                            ),
                            html.Div(
                                id="time",
                                className="mini_container",
                                children=[
                                    html.P("Time"),
                                    html.H6(f"{round((sum(strava_data['elapsed minutes']))/60,2)} hrs")
                                ]
                            ),
                            html.Div(
                                id="elevation",
                                className="mini_container",
                                children=[
                                    html.P("Elevation"),
                                    html.H6(f"{round(sum(strava_data['Elevation Gain']),0)} m")
                                ]
                            ),
                        ]
                    )
                    
                ],
            ),
            
            html.Div(
                id="stacked-subplots-container",
                # className="row",
                style={"width": '28%' },
                children=[
                    generate_section_banner("Metrics Overtime"),
                    html.Div(
                        avg_pace_line.render(app, strava_data),
                         style={
                            "width": "100%",  # Specify the width
                            "flex": '1 1 auto',
                            "height": "45%",  # Specify the height
                            # "padding": "10px",
                        },
                    ),
                     html.Div(
                        max_hr_line.render(app, strava_data),
                         style={
                            "width": "100%",  # Specify the width
                            "flex": 1,
                            "height": "45%",  # Specify the height
                            # "padding": "10px",
                        },
                    ),
                    html.Div(
                        vo2_max_line.render(app, apple_data),
                         style={
                            "width": "100%",  # Specify the width
                            "flex": 1,
                            "height": "45%",  # Specify the height
                            # "padding": "10px",
                        },
                    ),
                ],
            ),
        ],
    )

# -------------------------------------------------------------------------

def build_bottom_panel():
    return html.Div(
        id="bottom-section-container",
        className="row",
        children=[
            # BUILDING THE PIE CHART
            html.Div(
                id="piechart-container",
                className="row",
                style={"width": '25%'},
                children=[
                    generate_section_banner("Training Activity Distribution"),
                    html.Div(
                        run_type_pie.render(app, strava_data),
                        style={
                            "width": "90%",  # Specify the width
                            "height": "70%",  # Specify the height
                            "padding": "10px",
                        },
                    )
                    
                ],
            ),
            
            html.Div(
                id="barchart-container",
                className="row",
                style={"width": '25%'},
                children=[
                    generate_section_banner("Total Distance Each Day of The Week"),
                    html.Div(
                        dist_dow_bar.render(app, strava_data),
                        style={
                            "width": "100%",  
                            "height": "70%", 
                            "padding": "10px",
                        },
                    ),
                ],
            ),
            
            html.Div(
                id="barchart-container",
                className="row",
                style={"width": '25%'},
                children=[
                    generate_section_banner("Training Hours Per Week"),
                    training_hrs_bar.render(app, strava_data)
                ],
            ),
        ],
    )

# -------------------------------------------------------------------------
# BUILDING THE DASHBOARD APP
app.layout = html.Div(
    id="big-app-container",
    children=[
        build_banner(),
        build_tabs(),
        build_top_panel(),
        build_bottom_panel(), 
    ],
    
)
    
    
if __name__ == '__main__':
    app.run_server(debug=True)
