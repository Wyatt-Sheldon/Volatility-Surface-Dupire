import yfinance as yf
import pandas as pd
from datetime import datetime

def download_options_data(ticker_symbol="AAPL", save_path="data/options.csv", max_expiries=5):
    ticker = yf.Ticker(ticker_symbol)
    options = ticker.options[:max_expiries]  # limit how many expiry dates we pull

    all_data = []

    for expiry in options:
        try:
            chain = ticker.option_chain(expiry)
            calls = chain.calls.copy()
            calls["expiration"] = pd.to_datetime(expiry)
            calls["T"] = (calls["expiration"] - datetime.utcnow()).dt.total_seconds() / (365 * 24 * 3600)
            calls = calls[["strike", "impliedVolatility", "lastPrice", "T"]].dropna()
            calls = calls[calls["impliedVolatility"] > 0]
            all_data.append(calls)
        except Exception as e:
            print(f"Skipping {expiry} due to error: {e}")

    if all_data:
        combined = pd.concat(all_data, ignore_index=True)
        combined.to_csv(save_path, index=False)
        print(f"✅ Saved {len(combined)} options to {save_path}")
    else:
        print("⚠️ No valid options data found.")

if __name__ == "__main__":
    download_options_data()

