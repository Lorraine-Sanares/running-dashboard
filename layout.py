from dash import Dash, html, dcc
from . import days_dropdown
import pandas as pd
from Components import dist_dow_bar
from Components import run_type_pie
from .strava_loader import DataSchema
from .import run_dist_dropdown
from . import run_type_dropdown
from . import avg_pace_line
from . import max_hr_line




def create_layout(app: Dash, data: pd.DataFrame) -> html.Div:
    return html.Div(
        className="app-div",
        # style={'backgroundColor':'#273746'},
        children=[
            
            build_banner(),
            build_tabs(),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    days_dropdown.render(app, data),
                    run_dist_dropdown.render(app, data),
                    run_type_dropdown.render(app, data),
                ]
            ),    
            dist_dow_bar.render(app, data),
            run_type_pie.render(app, data),
            avg_pace_line(app, data),
            max_hr_line(app, data), 
            
        ],
    )
    
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
                        label="Specification Settings",
                        value="tab1",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                    dcc.Tab(
                        id="Control-chart-tab",
                        label="Control Charts Dashboard",
                        value="tab2",
                        className="custom-tab",
                        selected_className="custom-tab--selected",
                    ),
                ],
            )
        ],
    )
