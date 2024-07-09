from dash import Dash, html, dcc
import plotly.express as px 
from dash.dependencies import Input, Output
from .strava_loader import DataSchema
from . import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.MAX_HR_LINE, "children"),
        [Input(ids.RUN_DIST_DROPDOWN, "value"), 
         Input(ids.RUN_TYPE_DROPDOWN, "value"),
        ]
    )
    
    def update_bar_chart(
            rundist: list[str], runtype: list[str],
    ) -> html.Div:
        filtered_data = data.query("rundist in @rundist and runtype in @runtype")
        if filtered_data.shape[0] == 0: # dimentionality, no data selected
            return html.Div("No data selected.")
        
        # Dropping irrelevant rows
        if set([6, 7,]).issubset(filtered_data.index):
            filtered_data = filtered_data.drop(index=[6, 7])
        filtered_data = filtered_data.sort_values(by='start_date')
        
        fig = px.line(
            filtered_data,
            x=DataSchema.DATE,
            y=DataSchema.MAXHR,
            markers=True,
           
        )
        #fc4c02 - orange
        fig.update_traces(
            line_color="#2afebd",
            marker_color="#2afebd",
            marker_line_color="#2afebd",
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_x=0.5,
            xaxis_title=None,
            height=200,
            xaxis_tickformat = '%d %B'
        )
        fig.update_xaxes(showgrid=False, zeroline=False)
        fig.update_yaxes(showgrid=False, zeroline=False)
        
        return html.Div(dcc.Graph(figure=fig),id=ids.MAX_HR_LINE) 
    return html.Div(id=ids.MAX_HR_LINE) 