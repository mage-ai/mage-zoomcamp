if 'callback' not in globals():
    from mage_ai.data_preparation.decorators import callback


@callback('success')
def success_callback(parent_block_data, **kwargs):
    # Do something cool
    print('🌞 all is well!')


@callback('failure')
def failure_callback(parent_block_data, **kwargs):
    # Send alert, trigger other pipeline, etc.
    print('🌧️ stormy skies ahead')
