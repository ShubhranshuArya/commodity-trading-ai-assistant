from matplotlib import pyplot as plt
from matplotlib.dates import DateFormatter
import streamlit as st
from datetime import datetime, timedelta

from utils.sentiment_computing import (
    compute_daily_sentiment_score,
    pre_process_news_data,
)
from utils.data_fetching import fetch_stock_news, fetch_stock_price
from utils.util_functions import (
    get_stock_list,
    get_stock_news_topics,
    get_stock_news_list_sorting,
)


# Configure the page
st.set_page_config(
    page_title="Commodify",
    page_icon="🚀",
)

#####Sidebar Start#####

# Fetch and store commodity data
stock_list = get_stock_list()

# Add a new section for selecting stock
st.sidebar.markdown("## **Stock**")
stock = st.sidebar.selectbox(
    "Pick One",
    list(stock_list.keys()),
)

# Fetch and store commodity data
news_topic_list = get_stock_news_topics()

# Add a new section for selecting stock
st.sidebar.markdown("## **News Topics**")
news_topics = st.sidebar.multiselect(
    "Select Multiple",
    default="All",
    options=list(news_topic_list.keys()),
)

# Fetch and store commodity data
sort_by_list = get_stock_news_list_sorting()

# Add a new section for selecting stock
st.sidebar.markdown("## **Sort News**")
sort_by = st.sidebar.radio(
    "Pick One",
    options=sort_by_list,
    label_visibility="collapsed",
)
#####Sidebar End#####
st.markdown("# **🎲 Stock Sentiment Analysis**")
st.markdown("### **Free API limit exhausted**")

# #####Main Section Start#####

# st.markdown("# **🎲 Stock Sentiment Analysis**")
# st.markdown("##### **Analyze market sentiment from news data**")

# # Fetch the news and stock price data
# news_df = fetch_stock_news(stock, news_topics, sort_by)
# news_df = pre_process_news_data(news_df)
# df_daily = compute_daily_sentiment_score(news_df)
# stock_data = fetch_stock_price(stock)

# fig, ax1 = plt.subplots(figsize=(12, 6))

# # Plot the sentiment score on the first y-axis
# ax1.plot(df_daily.index, df_daily["score_ma"], color="blue", label="Sentiment 28d MA")

# ax1.set_xlabel("Date (m/y)", fontsize=16)
# ax1.set_ylabel("Sentiment", color="blue", fontsize=16)
# ax1.tick_params(axis="y", labelcolor="blue")

# # Increase the number of x-axis ticks
# ax1.xaxis.set_major_locator(plt.MaxNLocator(12))
# ax1.xaxis.set_major_formatter(DateFormatter("%m/%Y"))

# # Create the second y-axis
# ax2 = ax1.twinx()

# # Plot negative sentiment on the second y-axis
# ax2.plot(stock_data.index, stock_data["Close"], color="red", label="Close Price")

# ax2.set_ylabel("Price ($AUD)", color="red", fontsize=16)
# ax2.tick_params(axis="y", labelcolor="red")

# # Add legend
# lines1, labels1 = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=12)

# plt.title("Sentiment and Close Price Data for " + stock, fontsize=16)
# st.pyplot(fig)

# #####Main Section End#####
