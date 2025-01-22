import datetime as dt
import pandas as pd


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


def get_period_intervals():
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


def get_prediction_strategies():
    return ["ARIMA", "LSTM", "Hybrid"]


def get_backtesting_timeframes():
    timeframes = {
        "7 Days": pd.DateOffset(days=7),
        "15 Days": pd.DateOffset(days=15),
        "30 Days": pd.DateOffset(days=30),
        "45 Days": pd.DateOffset(days=45),
        "60 Days": pd.DateOffset(days=60),
    }
    return timeframes


def get_stock_news_topics():
    news_topics = {
        "All": "all",
        "Blockchain": "blockchain",
        "Earnings": "earnings",
        "IPO": "ipo",
        "Mergers & Acquisitions": "mergers_and_acquisitions",
        "Financial Markets": "financial_markets",
        "Economy - Fiscal Policy": "economy_fiscal",
        "Economy - Monetary Policy": "economy_monetary",
        "Economy - Macro/Overall": "economy_macro",
        "Energy & Transportation": "energy_transportation",
        "Finance": "finance",
        "Life Sciences": "life_sciences",
        "Manufacturing": "manufacturing",
        "Real Estate & Construction": "real_estate",
        "Retail & Wholesale": "retail_wholesale",
        "Technology": "technology",
    }
    return news_topics


def get_stock_list():
    stock_list = {
        "Apple": "AAPL",
        "Google": "GOOGL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Meta": "META",
    }

    return stock_list


def get_stock_news_list_sorting():
    stock_news_list_sorting = {
        "Relevance": "RELEVANCE",
        "Latest": "EARLIEST",
    }
    return stock_news_list_sorting
