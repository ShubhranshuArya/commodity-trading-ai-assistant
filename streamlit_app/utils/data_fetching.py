import yfinance as yf


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
