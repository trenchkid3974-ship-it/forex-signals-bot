"""
test_fetch.py — quick test: download EUR/USD and print the latest candles.
"""

import data_fetcher

candles = data_fetcher.fetch_candles("EUR/USD", "1h", outputsize=5)

print(f"SUCCESS — downloaded {len(candles)} candles for EUR/USD (1h)")
print("Oldest candle:", candles[0])
print("Newest candle:", candles[-1])
