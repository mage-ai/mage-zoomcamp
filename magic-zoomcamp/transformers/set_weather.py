if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

from mage_ai.data_preparation.variable_manager import set_global_variable

@transformer
def transform(data, *args, **kwargs):
    todays_weather = data[data.is_today]['weather'][0]
    
    set_global_variable('pipeline_variable_example', 'weather', todays_weather)



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
