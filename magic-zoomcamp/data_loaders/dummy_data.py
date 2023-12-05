if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd
from datetime import date, timedelta

@data_loader
def load_data(*args, **kwargs):
    fmt = '%Y-%m-%d'
    today = date.today().strftime(fmt)
    yesterday = (date.today() - timedelta(days=1)).strftime(fmt)

    weather_df = pd.DataFrame(
        {
            'date': [today, yesterday], 
            'weather': ['sunny', 'cloudy'],
            }
        )    
    
    weather_df['is_today'] = weather_df['date'].apply(lambda dt: dt == date.today().strftime(fmt))

    return weather_df
