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
    url = 'https://github.com/datablist/sample-csv-files/raw/main/files/customers/customers-500000.zip?raw=True'
    
    return pd.read_csv(url, sep=',', compression='zip')

@test
def test_rows(output, *args) -> None:
    """
    Check num rows in response
    """
    assert len(output) == 500000 , 'There are a different number of rows than expected!'


@test
def test_uniqueness(output, *args) -> None:
    """
    Test all Id's are unique
    """
    assert True not in output['Customer Id'].duplicated().unique() , 'There are duplicate Ids!'
