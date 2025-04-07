import yfinance as yf

def score_tradfi(ticker):
    stock = yf.Ticker(ticker)
    info = stock.info
    pe = info.get("trailingPE", 0)
    roe = info.get("returnOnEquity", 0)
    score = 0
    if pe and pe < 15:
        score += 15
    elif pe and pe < 25:
        score += 10
    else:
        score += 5
    if roe and roe > 0.15:
        score += 15
    elif roe and roe > 0.1:
        score += 10
    else:
        score += 5
    return {"ticker": ticker, "score": score}
