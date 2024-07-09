from dash import Dash, html, dcc
import plotly.graph_objects as go # for pie chart?
import plotly.express as px 
from dash.dependencies import Input, Output
from .strava_loader import DataSchema
from . import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.RUN_TYPE_PIE, "children"),
        Input(ids.RUN_TYPE_DROPDOWN, "value"),
    )
    
    def update_pie_chart(
        runtype: list[str]
    ) -> html.Div:
        filtered_data = data.query("runtype in @runtype")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected.")
        
        filtered_data.sort_values(DataSchema.DISTANCE, ascending=False)
        
        colourmap = ['#2AFEBD', '#2EC99B', '#31937A', '#355E58']
        # colourmap = ['#2AFEBD', '#2CE3AC', '#2EC99B', '#30AE8B', '#31937A', '#337969', '#355E58']
        # colourmap = ['#355E58', '#31937A', '#2EC99B', '#C9FFEF']
        
        fig = px.pie(
            filtered_data, 
            names=DataSchema.RUNTYPE,
            values=DataSchema.DISTANCE,
            hole=0.5,
            color=DataSchema.RUNTYPE,
            color_discrete_sequence=colourmap
        )

        fig.update_layout(
            margin={"t": 20, "b": 20, "l": 20, "r": 20},
            autosize=True,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font={"color": "white"},
            showlegend=False,
        )
        
        return html.Div(dcc.Graph(figure=fig), id=ids.RUN_TYPE_PIE)
    return html.Div(id=ids.RUN_TYPE_PIE)