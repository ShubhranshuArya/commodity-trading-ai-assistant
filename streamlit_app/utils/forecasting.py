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
