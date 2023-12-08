import yfinance as yf

def prices_yahoo(x, s, e):
  
  new_df = pd.DataFrame(yf.Ticker(x).history(start=s, end=e)).iloc[:,3]
  
  print(new_df)
  
prices_yahoo("AIG", "2010-05-31", "2021-01-30")
