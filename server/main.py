import uvicorn
from typing import List, Dict
from fastapi import FastAPI, File, Form, HTTPException, Body
from starlette.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import datetime
from data.alpaca import (
    get_stock_bars, get_stock_latest_bar, get_crypto_latest_bar, get_crypto_bars
)


app = FastAPI()

PORT = 5000

origins = [
    f"http://localhost:{PORT}",
    "https://chat.openai.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def _get_prices_helper(tickers):
    print(f"Getting prices for {tickers}")
    tickers = tickers.split(",")
    # filter out BTC/USD and ETH/USD from tickers
    crypto_tickers = [t for t in tickers if "USD" in t]
    stock_tickers = [t for t in tickers if "USD" not in t]
    # get stock prices
    stock_prices = get_stock_latest_bar(stock_tickers) if len(stock_tickers) > 0 else {}
    # get crypto prices
    crypto_prices = get_crypto_latest_bar(crypto_tickers) if len(crypto_tickers) > 0 else {}
    # merge stock and crypto prices (dictionaries)
    prices = {**stock_prices, **crypto_prices}
    return prices


@app.post("/get_prices", response_model=Dict)
async def get_prices(tickers: str):
    return _get_prices_helper(tickers)


@app.route("/.well-known/ai-plugin.json")
async def get_manifest(request):
    file_path = "./server/ai-plugin.json"
    return FileResponse(file_path, media_type="text/json", headers={"Cache-Control": "no-store"})


@app.route("/.well-known/logo.png")
async def get_logo(request):
    file_path = "./server/logo.png"
    return FileResponse(file_path, media_type="text/json", headers={"Cache-Control": "no-store"})


@app.route("/.well-known/openapi.yaml")
async def get_openapi(request):
    file_path = "./server/openapi.yaml"
    return FileResponse(file_path, media_type="text/json", headers={"Cache-Control": "no-store"})


@app.on_event("startup")
async def startup():
    print("Starting up...")


def start():
    uvicorn.run("server.main:app", host="localhost", port=PORT, reload=True)
