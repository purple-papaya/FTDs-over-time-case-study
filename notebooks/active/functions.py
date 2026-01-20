import pandas as pd
from IPython.display import display


def load_csv(file_path, delimiter=';', parse_dates=None, date_format='ISO8601'):
    '''
    Load CSV file with configurable parsing settings.
    '''
    if parse_dates:
        return pd.read_csv(file_path, delimiter=delimiter, parse_dates=parse_dates, date_format=date_format)
    else:
        return pd.read_csv(file_path, delimiter=delimiter)

def check_expected_columns(df, df_name, columns_list):
    '''
    Checks if expected columns are present.
    '''
    display(f'Are all expected columns in {df_name}?')
    return set(df.columns) == set(columns_list)

def check_dataframe_info(df, df_name):
    '''
    Checks data types.
    '''
    display(f'Data types of {df_name}:')
    return df.info()

def verify_uniqueness_constraints(df, df_name, column):
    '''
    Checks if critical columns are unique.
    '''
    display(f'Are all critical columns in {df_name} unique?')
    return df[column].is_unique