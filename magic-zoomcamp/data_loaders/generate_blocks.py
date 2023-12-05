from typing import Dict, List

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs) -> List[List[Dict]]:
    return [[{"id": i} for i in range(1,4)]]