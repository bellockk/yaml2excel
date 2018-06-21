import os
import logging
import pandas as pd
import yaml


def excel2yaml(target, source):
    sheets = pd.read_excel(source, sheet_name=None)
    if not os.path.exists(target):
        os.makedirs(target)
    for key, value in sheets.items():
        filename = os.path.join(target, '{0}.yaml'.format(key))
        logging.info('  Writing YAML: %s', filename)
        with open(filename, 'w') as f:
            f.write(yaml.safe_dump({key: value.fillna('').to_dict('records')},
                                   default_flow_style=False))
