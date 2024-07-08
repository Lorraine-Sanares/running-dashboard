from dash import Dash, html, dcc
import plotly.express as px # for bar chart
from dash.dependencies import Input, Output
from .strava_loader import DataSchema
from . import ids
import pandas as pd


# def activity_text(app: Dash, data: pd.DataFrame) -> html.Div:
    
# # -----------------------------------------------------------
# # still working on the dropdown functionality

#     # @app.callback(
#     #     Output(ids.ACTIVITY_TEXT, "children"),
#     #     [
#     #         # Input(ids.DAYS_DROPDOWN, "value"),
#     #         Input(ids.RUN_TYPE_DROPDOWN, "value"),
#     #         Input(ids.RUN_DIST_DROPDOWN, "value"),
#     #     ]
#     # )
#     # def update_activity_text(
#     #         # dayofweek: list[str],
#     #         rundist: list[str], 
#     #         runtype: list[str],
#     # ) -> html.Div:

#     #     filtered_data = data.query("runtype in @runtype or rundist in @rundist")
#     #     # print("filtered data")
#     #     # print(filtered_data)
#     #     if filtered_data.shape[0] == 0:  # dimensionality, no data selected
#     #         return html.Div("No data selected.")
      
#     #     activity_text = str(len(filtered_data))
#     #     return html.Div(activity_text)
    
#         activity_text = str(len(data))
        
#     # Initial layout
#     return html.Div(activity_text, id=ids.ACTIVITY_TEXT)




def time_text () -> html.H6:
    return

def elevation_text () -> html.H6:
    return


