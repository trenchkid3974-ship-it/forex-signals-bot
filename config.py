"""
config.py — all settings for the bot in one place.

SECURITY: no API keys or tokens in this file!
Secrets arrive from GitHub Secrets through environment variables.
"""

import os

# ---- Forex pairs the bot watches (add or remove freely) ----
PAIRS = [
    "EUR/USD", "GBP/USD", "USD/JPY", "USD/CHF", "AUD/USD",
    "NZD/USD", "USD/CAD", "EUR/GBP", "EUR/JPY", "GBP/JPY",
    "XAU/USD",
]

# ---- Timeframes ----
ALL_TIMEFRAMES = ["5min", "15min", "30min", "1h", "4h", "1day"]
SIGNAL_TIMEFRAMES = ["15min", "1h", "4h"]  # signals are generated on these

# ---- Market data API keys (from GitHub Secrets, never hardcoded) ----
TWELVEDATA_API_KEY = os.getenv("TWELVEDATA_API_KEY", "")
FINNHUB_API_KEY = os.getenv("FINNHUB_API_KEY", "")

# ---- Twelve Data free-plan safety limits ----
CANDLES_TO_FETCH = 200        # how much history the analysis uses
REQUEST_DELAY_SECONDS = 9     # free plan allows ~8 requests/minute

# ---- Signal quality controls (anti-spam) ----
MIN_CONFIDENCE = 65           # minimum strategy score (0-100) to publish
MAX_SIGNALS_PER_RUN = 3       # never flood the channel
SIGNAL_EXPIRY_HOURS = 24      # stop monitoring old signals

# ---- Feature switches ----
SEND_VOICE_NOTES = True       # set False to disable voice notes
