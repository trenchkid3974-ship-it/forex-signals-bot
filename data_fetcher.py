"""
data_fetcher.py — downloads real Forex candle data from Twelve Data.
"""

import time
import requests
import config


def fetch_candles(pair: str, timeframe: str, outputsize: int = None) -> list:
    """
    Download candles for one pair on one timeframe.

    Returns a list of candles, OLDEST first:
        [{"datetime": "...", "open": 1.10, "high": 1.12,
          "low": 1.09, "close": 1.11}, ...]
    """
    if not config.TWELVEDATA_API_KEY:
        raise ValueError("TWELVEDATA_API_KEY is missing — check your GitHub Secret.")

    size = outputsize or config.CANDLES_TO_FETCH
    url = "https://api.twelvedata.com/time_series"
    params = {
        "symbol": pair,
        "interval": timeframe,
        "outputsize": size,
        "apikey": config.TWELVEDATA_API_KEY,
    }

    response = requests.get(url, params=params, timeout=30)
    data = response.json()

    if "values" not in data:
        raise RuntimeError(f"Twelve Data error for {pair} ({timeframe}): {data}")

    candles = []
    for row in reversed(data["values"]):  # API gives newest first -> flip it
        candles.append({
            "datetime": row["datetime"],
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"]),
        })
    return candles


def fetch_all_pairs(timeframes: list) -> dict:
    """Fetch every pair on every timeframe. Slow on purpose (rate-limit safe)."""
    result = {}
    for pair in config.PAIRS:
        result[pair] = {}
        for tf in timeframes:
            try:
                result[pair][tf] = fetch_candles(pair, tf)
            except Exception as exc:
                print(f"WARNING: failed to fetch {pair} {tf}: {exc}")
                result[pair][tf] = []
            time.sleep(config.REQUEST_DELAY_SECONDS)
    return result
