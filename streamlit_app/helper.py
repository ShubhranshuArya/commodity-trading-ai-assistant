# Imports
import datetime as dt
import os
from pathlib import Path

# Import pandas
import pandas as pd

# Import yfinance
import yfinance as yf

# Import the required libraries
from statsmodels.tsa.ar_model import AutoReg


def get_commodity_types():
    return ["Precious Metals", "Energy", "Grains", "Soft Commodities"]


def get_commodities_by_type(commodity_type):
    commodities_by_type = {
        "Precious Metals": {
            "Gold": "GC=F",
            "Silver": "SI=F",
            "Platinum": "PL=F",
            "Palladium": "PA=F",
        },
        "Energy": {
            "Crude Oil": "CL=F",
            "Heating Oil": "HO=F",
            "Gasoline": "RB=F",
            "Natural Gas": "NG=F",
            "Brent Crude": "BZ=F",
        },
        "Grains": {
            "Corn": "ZC=F",
            "Oats": "ZO=F",
            "Wheat": "KE=F",
            "Rice": "ZR=F",
            "Composite": "ZM=F",
            "Soyabean": "ZS=F",
            "Soyabean Oil": "ZL=F",
        },
        "Soft Commodities": {
            "Cocoa": "CC=F",
            "Coffee": "KC=F",
            "Cotton": "CT=F",
            "Sugar": "SB=F",
        },
    }

    return commodities_by_type[commodity_type]


# Create function to fetch periods and intervals
def fetch_periods_intervals():
    # Create dictionary for periods and intervals
    periods = {
        "1d": ["1m", "2m", "5m", "15m", "30m", "60m", "90m"],
        "5d": ["1m", "2m", "5m", "15m", "30m", "60m", "90m"],
        "1mo": ["30m", "60m", "90m", "1d"],
        "3mo": ["1d", "5d", "1wk", "1mo"],
        "6mo": ["1d", "5d", "1wk", "1mo"],
        "1y": ["1d", "5d", "1wk", "1mo"],
        "2y": ["1d", "5d", "1wk", "1mo"],
        "5y": ["1d", "5d", "1wk", "1mo"],
        "10y": ["1d", "5d", "1wk", "1mo"],
        "max": ["1d", "5d", "1wk", "1mo"],
    }

    # Return the dictionary
    return periods


def fetch_prediction_timeframe():
    timeframes = {
        "24hrs": dt.timedelta(days=1),
        "1 Week": dt.timedelta(days=7),
        "1 Month": dt.timedelta(days=30),
        "3 Months": dt.timedelta(days=90),
    }
    return timeframes


# Function to fetch  commodity info
def fetch_commodity_info(commodity_ticker):
    # Pull the data for the first security
    commodity_data = yf.Ticker(commodity_ticker)

    # Extract full of the commodity
    commodity_data_info = commodity_data.info

    # Function to safely get value from dictionary or return "N/A"
    def safe_get(data_dict, key):
        return data_dict.get(key, "N/A")

    # Extract only the important information with new keys
    commodity_data_info_dict = {
        "Basic Information": {
            "shortName": safe_get(commodity_data_info, "shortName"),
            "symbol": safe_get(commodity_data_info, "symbol"),
            "underlyingSymbol": safe_get(commodity_data_info, "underlyingSymbol"),
            "quoteType": safe_get(commodity_data_info, "quoteType"),
            "currency": safe_get(commodity_data_info, "currency"),
            "exchange": safe_get(commodity_data_info, "exchange"),
            "timeZoneShortName": safe_get(commodity_data_info, "timeZoneShortName"),
        },
        "Price Information": {
            "previousClose": safe_get(commodity_data_info, "previousClose"),
            "open": safe_get(commodity_data_info, "open"),
            "dayLow": safe_get(commodity_data_info, "dayLow"),
            "dayHigh": safe_get(commodity_data_info, "dayHigh"),
            "regularMarketPreviousClose": safe_get(
                commodity_data_info, "regularMarketPreviousClose"
            ),
            "regularMarketOpen": safe_get(commodity_data_info, "regularMarketOpen"),
            "regularMarketDayLow": safe_get(commodity_data_info, "regularMarketDayLow"),
            "regularMarketDayHigh": safe_get(
                commodity_data_info, "regularMarketDayHigh"
            ),
        },
        "Volume Information": {
            "volume": safe_get(commodity_data_info, "volume"),
            "regularMarketVolume": safe_get(commodity_data_info, "regularMarketVolume"),
            "averageVolume": safe_get(commodity_data_info, "averageVolume"),
            "averageVolume10days": safe_get(commodity_data_info, "averageVolume10days"),
            "averageDailyVolume10Day": safe_get(
                commodity_data_info, "averageDailyVolume10Day"
            ),
        },
        "Bid-Ask Spread": {
            "bid": safe_get(commodity_data_info, "bid"),
            "ask": safe_get(commodity_data_info, "ask"),
            "bidSize": safe_get(commodity_data_info, "bidSize"),
            "askSize": safe_get(commodity_data_info, "askSize"),
        },
        "Historical and Benchmark Data": {
            "fiftyTwoWeekLow": safe_get(commodity_data_info, "fiftyTwoWeekLow"),
            "fiftyTwoWeekHigh": safe_get(commodity_data_info, "fiftyTwoWeekHigh"),
            "fiftyDayAverage": safe_get(commodity_data_info, "fiftyDayAverage"),
            "twoHundredDayAverage": safe_get(
                commodity_data_info, "twoHundredDayAverage"
            ),
        },
    }

    # Return the commodity data
    return commodity_data_info_dict


# Function to fetch the commodity history
def fetch_commodity_history(commodity_ticker, period, interval):
    # Pull the data for the first security
    commodity_data = yf.Ticker(commodity_ticker)

    # Extract full of the commodity
    commodity_data_history = commodity_data.history(period=period, interval=interval)[
        ["Open", "High", "Low", "Close"]
    ]

    # Return the commodity data
    return commodity_data_history


# Function to generate the commodity prediction
def generate_commodity_price_prediction(commodity_ticker, forecast_timeframe):
    # Try to generate the predictions
    try:
        # Pull the data for the first security
        commodity_data = yf.Ticker(commodity_ticker)

        # Extract the data for last 2yr with 1d interval
        commodity_data_hist = commodity_data.history(period="2y", interval="1d")

        # Clean the data for to keep only the required columns
        commodity_data_close = commodity_data_hist[["Close"]]

        # Change frequency to day
        commodity_data_close = commodity_data_close.asfreq("D", method="ffill")

        # Fill missing values
        commodity_data_close = commodity_data_close.ffill()

        # Define training and testing area
        train_df = commodity_data_close.iloc[
            : int(len(commodity_data_close) * 0.9) + 1
        ]  # 90%
        test_df = commodity_data_close.iloc[
            int(len(commodity_data_close) * 0.9) :
        ]  # 10%

        # Define training model
        model = AutoReg(train_df["Close"], 250).fit(cov_type="HC0")

        # Predict data for test data
        predictions = model.predict(
            start=test_df.index[0], end=test_df.index[-1], dynamic=True
        )

        # Predict timeframe into the future
        forecast = model.predict(
            start=test_df.index[0],
            end=test_df.index[-1] + dt.timedelta(days=1),
            dynamic=True,
        )

        # Return the required data
        return train_df, test_df, forecast, predictions

    # If error occurs
    except:
        # Return None
        return None, None, None, None
