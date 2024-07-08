from dash import Dash, html, dcc
import plotly.express as px # for bar chart
from dash.dependencies import Input, Output
from .strava_loader import DataSchema
from . import ids
import pandas as pd

# months = ["December", "January", "April", "May", "June"]    

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    @app.callback(
        Output(ids.TRAINING_HRS_BAR, "children"),
        Input(ids.DAYS_DROPDOWN, "value"), # bar chart is fitered by selected values
    )
    
    def update_bar_chart(
            dayofweek: list[str],
    ) -> html.Div:
        filtered_data = data.query("dayofweek in @dayofweek")
        if filtered_data.shape[0] == 0: # dimentionality, no data selected
            return html.Div("No data selected.")
        
        hrs_per_week = pd.DataFrame({'week': filtered_data[DataSchema.WEEK], 'elapsed hours': filtered_data['elapsed minutes']})
        # def create_pivot_table() -> pd.DataFrame:
        #     pt = filtered_data.pivot_table(
        #         values=filtered_data, # y values
        #         index=[DataSchema.WEEK,], #DataSchema.DAYNUM], # x values
        #         aggfunc="sum",
        #         fill_value=0 
        #     )
        #     return pt.reset_index().sort_values(DataSchema.DAYNUM, ascending=True)
        
        fig = px.bar(
            # create_pivot_table(),
            hrs_per_week,
            x=hrs_per_week['elapsed hours'],
            y=DataSchema.WEEK,
            text_auto='.2s', 
            orientation='h',
           
        )
        
        
        fig.update_traces(textfont_size=12, 
                textangle=0, 
                textposition="outside", 
                cliponaxis=False,
                marker_color="#fc4c02",
                marker_line_color='#fc4c02'
        )

        fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color='white'),
                title_x=0.5,
                yaxis_title='Distance (km)',
                autosize=True,
        )
        
        return html.Div(dcc.Graph(figure=fig),id=ids.TRAINING_HRS_BAR) 
    return html.Div(id=ids.TRAINING_HRS_BAR) 