from dash import Dash, html, dcc
# dcc collection of user interface components by dash
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from .strava_loader import DataSchema
# from app import generate_section_banner

def render(app: Dash, data: pd.DataFrame) -> html.Div: 
    
    run_type = ['Recovery run', 'Zone 2', 'Speed run', 'Long run']
    unique_run_types = sorted(set(run_type), key=str) # since there are multiple runs in same month
    
    @app.callback(
        Output(ids.RUN_TYPE_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_RUN_TYPES_BUTTON, "n_clicks"),
    )
    
    def select_all_run_types(_: int) -> list[str]:
        return unique_run_types
    
    return html.Div(
        children=[
            dcc.Dropdown(
                id=ids.RUN_TYPE_DROPDOWN,
                options=[{"label": run, "value": run} for run in unique_run_types],
                value=unique_run_types,
                multi=True,
            ),
            html.Button(
                id=ids.SELECT_ALL_RUN_TYPES_BUTTON,
                className="dropdown-button",
                children=['Select All'],
                n_clicks=0,
                style={"color": "darkgray"},
            )
        ]
    )