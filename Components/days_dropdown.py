from dash import Dash, html, dcc
from . import ids
from dash.dependencies import Input, Output
import pandas as pd
from .strava_loader import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div: 
    
    all_days: list[str] = data[DataSchema.DAYOFWEEK].tolist()
    unique_days = sorted(set(filter(None, all_days)), key=str) # Filter out None values and sort
    
    @app.callback(
        Output(ids.DAYS_DROPDOWN, "value"),
        Input(ids.SELECT_ALL_DAYS_BUTTON, "n_clicks"),
    )
    
    def select_all_nations(_: int) -> list[str]:
        return unique_days
    
    return html.Div(
        children=[
            dcc.Dropdown(
                id=ids.DAYS_DROPDOWN,
                options=[{"label": day, "value": day} for day in unique_days],
                value=unique_days,
                multi=True,
            ),
            
            html.Button(
                id=ids.SELECT_ALL_DAYS_BUTTON,
                className="dropdown-button",
                children=['Select All'],
                n_clicks=0,
                style={"color": "darkgray"},
            ),
        ],
    )