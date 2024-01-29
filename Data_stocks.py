import yfinance as yf
import pandas as pd

"""
nvidia - 1999, sap -- "NVDA"
dominos pizza group - 1999 , FTSE  --- "DPZ"
Garmin - 2000 -- "GRMN"
GameStop - 2002 -- "GME"
Netflix -  2002 -- "NFLX"
PayPal - 2002 -- "PYPL"
GOOGLE - 2004 -- "GOOG"
Under Armour - 2005 -- "UA"
BOOking Holding - 1999 -- "BKNG"
EPSON - 2003 -- "SEKEY"
S&P500 -- "^GSPC"
"""

stock = "^GSPC"
bond = "^TYX"
od = "2016-01-01"
do = "2023-12-31"
interval = "1mo"
file_path = f"{stock}_output_main.csv"


def data_download(name):
    raw_data = yf.download (tickers = name, start = od,
                              end = do, interval = interval)
    return raw_data
def price_volume(set):
    novy = set.iloc[:,[-2,-1]]
    return novy

def returncompute(stock, bond):
    merged_data = pd.merge(stock, bond, how='inner', on='Date', suffixes=('_stock', '_bond'))
    merged_data['Stock_Returns'] = merged_data['Adj Close_stock'].pct_change().dropna()
    merged_data['Bond_Adjusted'] = merged_data['Adj Close_bond'] / 100
    merged_data['Excess_Returns'] = merged_data['Stock_Returns'] - merged_data['Bond_Adjusted'].pct_change().dropna()
    return merged_data

def dataframe_to_csv(dataframe, file_path, index=True):

    try:
        dataframe.to_csv(file_path, index=index)
        return f"DataFrame has been successfully saved to {file_path}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

tbond = data_download(bond)
tbond_adj = tbond.iloc[:,-2]
sap = data_download(stock)
mensi = price_volume(sap)
data_a_returns = returncompute(mensi, tbond_adj)
data_a_returns_reset_index = data_a_returns.reset_index()
dataframe_to_csv(data_a_returns_reset_index, file_path)


