from dash import Dash, html, dcc
import plotly.graph_objects as go # for pie chart?
import plotly.express as px # for bar chart
from dash.dependencies import Input, Output
# from ..Components.loader import DataSchema
from .strava_loader import DataSchema
from . import ids
import pandas as pd

# months = ["December", "January", "April", "May", "June"]    
    
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
        
        filtered_data.reset_index().sort_values(DataSchema.DISTANCE, ascending=False)

        fig = px.pie(
            filtered_data, #.sort_values(by=DataSchema.DISTANCE, ascending=False),
            names=DataSchema.RUNTYPE,
            values=DataSchema.DISTANCE,
            hole=0.5,
            color=DataSchema.DISTANCE,
            color_discrete_sequence=px.colors.sequential.Oranges_r
        )

        fig.update_layout(margin={"t": 20, "b": 20, "l": 20, "r": 20},
                          autosize=True,
                          paper_bgcolor='rgba(0,0,0,0)',
                          plot_bgcolor='rgba(0,0,0,0)',
                          font={"color": "white"},
                          showlegend=False,
                        )
        
        return html.Div(dcc.Graph(figure=fig), id=ids.RUN_TYPE_PIE)

    return html.Div(id=ids.RUN_TYPE_PIE)