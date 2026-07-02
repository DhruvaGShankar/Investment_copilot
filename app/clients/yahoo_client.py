import yfinance as yf

class YahooClient:
     
     @staticmethod
     def get_ticker(ticker: str):
         return yf.Ticker(ticker)