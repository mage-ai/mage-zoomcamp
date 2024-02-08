import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{}.csv.gz'
    
    taxi_dtypes = {
                'VendorID': pd.Int64Dtype(),
                'passenger_count': pd.Int64Dtype(),
                'trip_distance': float,
                'RatecodeID':pd.Int64Dtype(),
                'store_and_fwd_flag':str,
                'PULocationID':pd.Int64Dtype(),
                'DOLocationID':pd.Int64Dtype(),
                'payment_type':pd.Int64Dtype(),
                'fare_amount': float,
                'extra':float,
                'mta_tax':float,
                'tip_amount':float,
                'tolls_amount':float,
                'improvement_surcharge':float,
                'total_amount':float,
                'congestion_surcharge':float,
                'ehail_fee':float,
                'trip_type':pd.Int64Dtype()

            }
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    fianl_quarter_2020_data = pd.DataFrame()

    for month in range (10, 13):
        url = base_url.format(month)
        current_month_data = pd.read_csv(url, sep=",", compression="gzip", dtype=taxi_dtypes, parse_dates=parse_dates )
        fianl_quarter_2020_data = pd.concat([fianl_quarter_2020_data, current_month_data], ignore_index=True)
    
    return fianl_quarter_2020_data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
