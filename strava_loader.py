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
    
    run_data = data.copy()
    
    # merging the dataframes by activity date
    run_data['Activity Date'] = pd.to_datetime(run_data['Activity Date'],format='%d %b %Y, %H:%M:%S')
    run_data['start_date'] = run_data['Activity Date'].dt.date
    run_data["months"] = run_data[DataSchema.DATE].dt.month_name()
    run_data["year"] = run_data[DataSchema.DATE].dt.year 
    run_data["dayofweek"] = run_data[DataSchema.DATE].dt.day_name()
    run_data["daynum"] = run_data[DataSchema.DATE].dt.dayofweek
    run_data['elapsed minutes'] = round(run_data['Elapsed Time']/60, 2)
    run_data['km per hour'] = round(run_data['Distance'] / (run_data['elapsed minutes'] / 60), 2)
    run_data['avg pace'] = round(run_data['elapsed minutes'] / run_data['Distance'], 2)
    run_data['week'] = run_data['Activity Date'].dt.isocalendar().week
    
    
    
    # print('removing walks')
    # print(run_data)
    def run_type(data):
        run_data['runtype'] = 'unknown'
        for i, name in enumerate(run_data['Activity Name']):
            if "Recovery" in name:
                run_data.at[i, 'runtype'] = 'Recovery run'
            elif "Speed" in name:
                run_data.at[i, 'runtype'] = 'Speed run'
            elif "Long" in name:
                run_data.at[i, 'runtype'] = 'Long run'
            else:
                run_data.at[i, 'runtype'] = 'Recovery run'
        
        for i, heart_rate in enumerate(run_data['Max Heart Rate']):
            if heart_rate < 170:
                run_data.at[i, 'runtype'] = 'Zone 2'
        return run_data

    def run_dist(data):
        run_data['rundist'] = 'other'
        
        for i, dist in enumerate(run_data[DataSchema.DISTANCE]):
            if (1 <= dist < 2):
                run_data.at[i, 'rundist'] = '1km'
            elif 3 <= dist < 4:
                run_data.at[i, 'rundist'] = '3km'
            elif 5 <= dist < 6:
                run_data.at[i, 'rundist'] = '5km'  
            elif 10 <= dist < 1:
                run_data.at[i, 'rundist'] = '10km'
        return run_data
    
    run_type(run_data)
    run_dist(run_data)
    
    return run_data
    