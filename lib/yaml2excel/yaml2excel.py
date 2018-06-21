import os
import logging
import pandas as pd
import yaml


def to_excel(target, source):
    files = [f for f in os.listdir(source) if f.lower().endswith('.yaml')]
    logging.info('  Opening excel file for writing: %s', target)
    writer = pd.ExcelWriter(target)
    for f in files:
        logging.info('  Processing YAML: %s', f)
        with open(f, 'r') as f_obj:
            data = yaml.load(f_obj)
        sheet_key = [k for k in data.keys() if not k.startswith('_')][0]
        logging.info('  Found Table: %s', sheet_key)
        sheet_df = pd.DataFrame(data[sheet_key])
        sheet_df.to_excel(writer, sheet_key, index=False, freeze_panes=(1, 0))
    logging.info('  Writing Metadata:')
    logging.info('  Closing excel file for writing: %s', target)
    writer.save()
