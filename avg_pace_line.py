from dash import Dash, html, dcc
import plotly.express as px # for bar chart
from dash.dependencies import Input, Output
from .strava_loader import DataSchema
from . import ids
import pandas as pd

  

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.AVG_PACE_LINE, "children"),
        [Input(ids.RUN_DIST_DROPDOWN, "value"), 
         Input(ids.RUN_TYPE_DROPDOWN, "value")
        ]
    )
    
    
    
    def update_bar_chart(
            rundist: list[str], runtype: list[str],
    ) -> html.Div:
        filtered_data = data.copy()
        
        
        filtered_data = data.query("rundist in @rundist and runtype in @runtype")
        if filtered_data.shape[0] == 0: # dimentionality, no data selected
            return html.Div("No data selected.")
        
        # Dropping specified rows
        if set([6, 7,]).issubset(filtered_data.index):
            filtered_data = filtered_data.drop(index=[6, 7])
        
        # print('avg pace removing old dates')
        # print(filtered_data)
        fig = px.line(
            filtered_data,
            x=DataSchema.DATE,
            y=DataSchema.AVGPACE,
            markers=True,
           
        )
        
        fig.update_traces(
            line_color="#fc4c02",
            marker_color="#fc4c02",
            marker_line_color="#fc4c02",
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
        fig.update_xaxes(showgrid=False, 
                         zeroline=False,) 
                        #  tickangle=-180,)
        fig.update_yaxes(showgrid=False, zeroline=False)
        
        return html.Div(dcc.Graph(figure=fig),id=ids.AVG_PACE_LINE) 
    return html.Div(id=ids.AVG_PACE_LINE,) 