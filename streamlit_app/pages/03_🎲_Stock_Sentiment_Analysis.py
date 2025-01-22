import streamlit as st
from datetime import datetime, timedelta

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
news_topic_list = get_stock_news_list_sorting()

# Add a new section for selecting stock
st.sidebar.markdown("## **Sort News**")
news_topics = st.sidebar.radio(
    "Pick One",
    options=news_topic_list,
    label_visibility="collapsed",
)
#####Sidebar End#####


#####Main Section Start#####
# Title
st.markdown("# **🎲 Stock Sentiment Analysis**")

# Subtitle
st.markdown("##### **Analyze market sentiment from news data**")
#####Main Section End#####
