import yfinance as yf
import pandas as pd

def prices_yahoo(y, s=None, e=None):
    p = pd.DataFrame()  # Create an empty DataFrame

    # Loop for data extraction & Set up statements for start and end dates
    for ticker in y:
        if s is None and e is None:
            # When neither start date nor end date is defined
            data = yf.download(ticker)
        elif e is None:
            data = yf.download(ticker, start=s) # Only start date is defined
        elif s is None:
            data = yf.download(ticker, end=e)  # When only end date is defined
        else:
            # When both start date and end date are defined
            data = yf.download(ticker, start=s, end=e)

        # Extract the Adjusted Close prices and add to the DataFrame
        if not data.empty:
            p[ticker] = data['Adj Close']

    p = p.dropna() # Drop rows with NA values

    return p

result = prices_yahoo(y=["UNM", "AIG", "OMF", "MET", "HIG"], s="2022-01-01")
print(result) # Test
