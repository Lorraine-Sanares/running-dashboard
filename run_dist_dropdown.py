from dash import Dash, html, dcc
# dcc collection of user interface components by dash
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from .strava_loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div: 
    # run_dist = ['1km', '3km', '5km', '10km', 'other']
    run_dist = ['1km', '3km', '5km', '10km']
    unique_run_dist = sorted(set(run_dist), key=str) # since there are multiple runs in same month
    
    @app.callback(
        Output(ids.RUN_DIST_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_RUN_DIST_BUTTON, "n_clicks"),
    )
    
    def select_all_run_types(_: int) -> list[str]:
        return unique_run_dist
    
    return html.Div(
        children=[
            # html.H6("Run Distances"),
            dcc.Dropdown(
                id=ids.RUN_DIST_DROPDOWN,
                options=[{"label": run, "value": run} for run in unique_run_dist],
                value=unique_run_dist,
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_RUN_DIST_BUTTON,
                className="dropdown-button",
                children=['Select All'],
                n_clicks=0,
                style={"color": "darkgray"},
            )
        ]
    )