from functions import load_csv

PATH = '../../data/raw/'

DATAFRAMES = {
    'df_trans': load_csv(PATH + 'trans.csv', parse_dates=['created_at']),
    'df_trader': load_csv(PATH + 'trader.csv'),
    'df_clients': load_csv(PATH + 'clients.csv', parse_dates=['_created_on']),
    'df_partner_codes': load_csv(PATH + 'partner_codes.csv'),
    'df_a2p_ref': load_csv(PATH + 'a2p_ref.csv')
} 

EXPECTED_COLUMNS = {
    'df_trans': ["transaction_id", "login", "created_at", "amount", "currency"],
    'df_trader': ["login", "client", "account_id", "first_deposit_id"],
    'df_clients': ["client", "client_id", "_created_on", "type"],
    'df_partner_codes': ["code", "partner_code_id"],
    'df_a2p_ref': ["ref_id", "account_id", "partner_code_id"]
}