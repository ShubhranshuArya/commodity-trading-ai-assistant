import pandas as pd


def pre_process_news_data(news_df):
    print(news_df.head(2))
    news_df = news_df[["time_published", "title", "summary", "overall_sentiment_score"]]
    news_df["time_published"] = pd.to_datetime(
        news_df["time_published"], format="%Y%m%dT%H%M%S"
    )
    news_df["score"] = news_df["overall_sentiment_score"]
    news_df.set_index("time_published", inplace=True)
    news_df.sort_index(
        ascending=False,
        inplace=True,
    )

    news_df.index = news_df.index.tz_localize(None)

    news_df = news_df[["score"]]

    return news_df


def compute_daily_sentiment_score(news_df):
    # Calculate median sentiment for everyday
    df_daily = news_df.resample("D").median()
    df_daily.fillna(0, inplace=True)

    # Count the number of entries per day
    df_daily_count = news_df.resample("D").size()

    # If you want to add this count to your existing df_daily DataFrame:
    df_daily["entry_count"] = df_daily_count
    df_daily["entry_count_ma"] = (
        df_daily["entry_count"].rolling(window=28, center=False).mean()
    )

    # Calculate a 28 day moving average of the score
    df_daily["score_ma"] = df_daily["score"].rolling(window=28, center=False).mean()

    return df_daily
