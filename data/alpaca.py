from alpaca.data import CryptoHistoricalDataClient, StockHistoricalDataClient
from alpaca.data.requests import StockLatestBarRequest, CryptoBarsRequest, StockBarsRequest, CryptoLatestBarRequest
from alpaca.data.timeframe import TimeFrame
from datetime import datetime, timedelta
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
endpoint = "https://paper-api.alpaca.markets"

crypto_client = CryptoHistoricalDataClient() # no keys required.
stock_client = StockHistoricalDataClient(API_KEY,  SECRET_KEY) # keys required


def get_stock_bars(symbols, start_dt=None, end_dt=None, timeframe=TimeFrame.Day):
  if end_dt is None:
    end_dt = datetime.now() - timedelta(minutes=15)

  if start_dt is None:
    start_dt = end_dt - timedelta(days=30)

  request_params = StockBarsRequest(
      symbol_or_symbols=symbols,
      timeframe=TimeFrame.Day,
      start=start_dt,
      end=end_dt
  )

  stock_bars = stock_client.get_stock_bars(request_params)

  return stock_bars.df

def get_crypto_bars(symbols, start_dt=None, end_dt=None, timeframe=TimeFrame.Day):
  if end_dt is None:
    end_dt = datetime.now()

  if start_dt is None:
    start_dt = end_dt - timedelta(days=30)

  request_params = CryptoBarsRequest(
                          symbol_or_symbols=symbols,
                          timeframe=TimeFrame.Day,
                          start=start_dt,
                          end=end_dt
                  )

  crypto_bars = crypto_client.get_crypto_bars(request_params)
  return crypto_bars.df


def get_stock_latest_bar(symbols):
  # multi symbol request - single symbol is similar
  multisymbol_request_params = StockLatestBarRequest(symbol_or_symbols=symbols)
  latest_multisymbol_bar = stock_client.get_stock_latest_bar(multisymbol_request_params)
  prices = {}
  for s in symbols:
    prices[s] = latest_multisymbol_bar[s].close

  return prices


def format_if_crypto_symbol(s):
    if "USD" not in s: return s
    return s if "/" in s else s[:3] + "/" + s[3:]


def get_crypto_latest_bar(symbols):
  # add / between BTC and USD e.g. BTCUSD -> BTC/USD if / is not present
  symbols = [ format_if_crypto_symbol(s) for s in symbols]
  crypto_quote_request = CryptoLatestBarRequest(symbol_or_symbols=symbols)
  latest_crypto_bar = crypto_client.get_crypto_latest_bar(crypto_quote_request)
  prices = {}
  for s in symbols:
    prices[s] = latest_crypto_bar[s].close 

  return prices

