from dash import Dash, html, dcc
import plotly.express as px 
from dash.dependencies import Input, Output
from .strava_loader import DataSchema
from . import ids
import pandas as pd

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.TRAINING_HRS_BAR, "children"),
        Input(ids.RUN_TYPE_DROPDOWN, "value"), # bar chart is fitered by selected values
    )
    
    def update_bar_chart(
            runtype: list[str],
    ) -> html.Div:

        df = pd.DataFrame(round((data.groupby('week')['elapsed minutes'].sum()/60), 1))
        df = df.reset_index()
        df = df.drop(index=[0,1,7])
        hrs_per_week = pd.DataFrame({'week': df['week'], 'elapsed hours': df['elapsed minutes']})
        
        fig = px.bar(
            hrs_per_week,
            x=hrs_per_week['elapsed hours'],
            y=DataSchema.WEEK,
            text='elapsed hours',
            orientation='h',
        )
        
        fig.update_traces(textfont_size=12, 
            textangle=0, 
            textposition="outside", 
            cliponaxis=False,
            marker_color="#2afebd",
            marker_line_color='#2afebd'
        )

        fig.update_layout(
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            font=dict(color='white'),
            title_x=0.5,
            yaxis_title='Week',
            autosize=True,
        )
        
        fig.update_yaxes(autorange='reversed')
        
        return html.Div(dcc.Graph(figure=fig),id=ids.TRAINING_HRS_BAR) 
    return html.Div(id=ids.TRAINING_HRS_BAR) 