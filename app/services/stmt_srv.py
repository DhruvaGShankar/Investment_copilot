from app.clients.yahoo_client import YahooClient

def get_fin_stmt(ticker: str):
    stock = YahooClient.get_ticker(ticker)
    
    return{
        "income_statement": stock.financials,
        "balance_sheet": stock.balance_sheet,
        "cash_flow": stock.cash_flow
    }