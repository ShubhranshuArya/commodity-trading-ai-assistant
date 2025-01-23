from statsmodels.tsa.ar_model import AutoReg
import yfinance as yf
import pandas as pd
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
import numpy as np


def commodity_forecast_backtesting(
    commodity_ticker,
    backtest_timeframe,
    selected_strategy,
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

        if selected_strategy == "ARIMA":
            # ------------------
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

        else:
            # Scale the data
            scaler = MinMaxScaler(feature_range=(0, 1))
            scaled_data = scaler.fit_transform(forecasting_data)

            # Prepare the data for LSTM
            def create_dataset(data, time_step=1):
                X, Y = [], []
                for i in range(len(data) - time_step - 1):
                    a = data[i : (i + time_step), 0]
                    X.append(a)
                    Y.append(data[i + time_step, 0])
                return np.array(X), np.array(Y)

            time_step = 60
            X, Y = create_dataset(scaled_data, time_step)
            X = X.reshape(X.shape[0], X.shape[1], 1)

            # Split into train and test
            train_size = int(len(X) * 0.9)
            train_X, test_X = X[:train_size], X[train_size:]
            train_Y, test_Y = Y[:train_size], Y[train_size:]

            # Build the LSTM model
            model = Sequential()
            model.add(LSTM(50, return_sequences=True, input_shape=(time_step, 1)))
            model.add(LSTM(50, return_sequences=False))
            model.add(Dense(1))
            model.compile(optimizer="adam", loss="mean_squared_error")

            # Train the model
            model.fit(train_X, train_Y, epochs=100, batch_size=64, verbose=1)

            # Predict
            test_predict = model.predict(test_X)
            test_predict = scaler.inverse_transform(test_predict.reshape(-1, 1))

            # Prepare predicted data for return
            predicted_data = pd.DataFrame(
                test_predict,
                index=forecasting_data.index[-len(test_predict) :],
                columns=["Close"],
            )

        # --------------
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
