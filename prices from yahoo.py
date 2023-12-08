import yfinance as yf

def prices_yahoo(x, s, e):
  
  print(yf.Ticker(x).history(start=s, end=e))
  
prices_yahoo("AIG", "2010-05-31", "2021-01-30")
