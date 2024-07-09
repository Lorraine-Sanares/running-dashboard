import pandas as pd

class DataSchema: 
    DATE = "Activity Date"
    MONTH = "months"
    YEAR = "year"
    DAYOFWEEK = "dayofweek"
    DISTANCE = "Distance"
    DAYNUM = "daynum"
    RUNTYPE = 'runtype'
    AVGPACE = 'avg pace'
    MAXHR = 'Max Heart Rate'
    WEEK = 'week'
    
def load_strava_data(path: str) -> pd.DataFrame:
    
    data = pd.read_csv(path)
        
    # merging the dataframes by activity date
    data['Activity Date'] = pd.to_datetime(data['Activity Date'],format='%d %b %Y, %H:%M:%S')
    data['start_date'] = data['Activity Date'].dt.date
    data["months"] = data[DataSchema.DATE].dt.month_name()
    data["year"] = data[DataSchema.DATE].dt.year 
    data["dayofweek"] = data[DataSchema.DATE].dt.day_name()
    data["daynum"] = data[DataSchema.DATE].dt.dayofweek
    data['elapsed minutes'] = round(data['Elapsed Time']/60, 2)
    data['km per hour'] = round(data['Distance'] / (data['elapsed minutes'] / 60), 2)
    data['avg pace'] = round(data['elapsed minutes'] / data['Distance'], 2)
    data['week'] = data['Activity Date'].dt.isocalendar().week
    
    # print('removing walks')
    # print(run_data)
    def run_type(data):
        data['runtype'] = 'unknown'
        # classifying run types
        for i, name in enumerate(data['Activity Name']):
            if "Recovery" in name:
                data.at[i, 'runtype'] = 'Recovery run'
            elif "Speed" in name:
                data.at[i, 'runtype'] = 'Speed run'
            elif "Long" in name:
                data.at[i, 'runtype'] = 'Long run'
            else:
                data.at[i, 'runtype'] = 'Recovery run'
        
        for i, heart_rate in enumerate(data['Max Heart Rate']):
            if heart_rate < 170:
                data.at[i, 'runtype'] = 'Zone 2'
        return data

    def run_dist(data):
        data['rundist'] = 'other'
        # classifying run distances
        for i, dist in enumerate(data[DataSchema.DISTANCE]):
            if (1 <= dist < 2):
                data.at[i, 'rundist'] = '1km'
            elif 3 <= dist < 4:
                data.at[i, 'rundist'] = '3km'
            elif 5 <= dist < 6:
                data.at[i, 'rundist'] = '5km'  
            elif 10 <= dist < 1:
                data.at[i, 'rundist'] = '10km'
        return data
    
    run_type(data)
    run_dist(data)
    
    return data
    