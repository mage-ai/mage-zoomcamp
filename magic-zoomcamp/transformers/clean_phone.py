import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    data.columns = (data.columns
                .str.replace(' ', '_', regex=True)
                .str.lower()
             )

    data['connection_method'] = data.apply(lambda row: row['website'].split('://')[0], axis=1)

    data = data[data['connection_method'] == 'https']
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
