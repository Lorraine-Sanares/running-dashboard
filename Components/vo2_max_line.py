from dash import Dash, html, dcc
import plotly.express as px 
from .apple_loader import DataSchema
from . import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:

    fig = px.line(
        data,
        x=DataSchema.DATE,
        y=DataSchema.VO2_MAX,
        markers=True,   
    )

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
        yaxis_title='VO2 Max',
        height=200
    )
    
    fig.update_xaxes(showgrid=False, zeroline=False)
    fig.update_yaxes(showgrid=False, zeroline=False)

    return html.Div(dcc.Graph(figure=fig),id=ids.VO2_MAX_LINE) 
    
