from statsmodels.tsa.ar_model import AutoReg
import yfinance as yf
import pandas as pd


def commodity_forecast_backtesting(
    commodity_ticker,
    backtest_timeframe,
    # selected_strategy,
):
    try:
        commodity_data = yf.Ticker(commodity_ticker)
        commodity_data_hist = commodity_data.history(period="2y", interval="1d")
        commodity_data_close = commodity_data_hist[["Close"]]
        commodity_data_close = commodity_data_close.asfreq("D", method="ffill")
        commodity_data_close = commodity_data_close.ffill()

        backtest_date = commodity_data_close.index[-1] - backtest_timeframe
        forecasting_data = commodity_data_close[
            commodity_data_close.index <= backtest_date
        ]
        original_data = commodity_data_close[commodity_data_close.index > backtest_date]

        train_df = forecasting_data.iloc[: int(len(forecasting_data) * 0.9) + 1]
        test_df = forecasting_data.iloc[int(len(forecasting_data) * 0.9) :]

        model = AutoReg(train_df["Close"], 250).fit(cov_type="HC0")

        backtest_end_date = test_df.index[-1] + backtest_timeframe
        predicted_data = model.predict(
            start=test_df.index[0],
            end=backtest_end_date,
            dynamic=True,
        )

        predicted_data = predicted_data[predicted_data.index > backtest_date]

        return original_data, predicted_data

    except:
        return None, None


# def compute_daily_stock_sentiment(
#     stock_ticker,
#     news_topics,
#     time_from,
#     time_to,
# ):
#     news_df = fetch_stock_news(stock_ticker, news_topics, time_from, time_to)
#     filtered_df = news_df[["title", "time_published", "summary"]]

#     # Calculate individual sentiment scores
#     filtered_df["sentiment"] = filtered_df["summary"].apply(textblob_sentiment_compute)

#     # Convert time_published to datetime
#     filtered_df["time_published"] = pd.to_datetime(filtered_df["time_published"])
#     filtered_df.set_index("time_published", inplace=True)

#     # Calculate daily median sentiment
#     daily_sentiment = filtered_df.resample("D").agg(
#         {
#             "sentiment": "median",
#             "title": "count",  # This gives us the number of articles per day
#         }
#     )

#     # Rename columns for clarity
#     daily_sentiment.columns = ["median_sentiment", "article_count"]

#     # Calculate rolling averages (28-day window as used in the notebook)
#     daily_sentiment["sentiment_ma"] = (
#         daily_sentiment["median_sentiment"].rolling(window=28, center=False).mean()
#     )
#     daily_sentiment["article_count_ma"] = (
#         daily_sentiment["article_count"].rolling(window=28, center=False).mean()
#     )

#     # Fill any NaN values with 0
#     daily_sentiment.fillna(0, inplace=True)

#     return daily_sentiment


# def textblob_sentiment_compute(text):
#     from textblob import TextBlob

#     return TextBlob(text).sentiment.polarity
