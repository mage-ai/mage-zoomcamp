from typing import Dict, List


@transformer
def transform(data: Dict, *args, **kwargs) -> List[Dict]:
    data['id'] = int(data['id']) ** 3
    return [data]