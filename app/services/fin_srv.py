from app.clients.yahoo_client import YahooClient

def get_company_info(ticker):
    stock = YahooClient.get_ticker(ticker)
    info = stock.info
    return {
        "company_name": info.get("longName"),
        "price": info.get("currentPrice"),
        "market_cap": info.get("marketCap"),
        "sector": info.get("sector"),
        "industry": info.get("industry"),
        "pe_ratio": info.get("trailingPE"),
        "eps": info.get("trailingEps"),
        "dividend_yield": info.get("dividendYield"),}
