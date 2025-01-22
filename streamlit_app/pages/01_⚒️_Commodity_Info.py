# Import streamlit
import streamlit as st
import pandas as pd

from utils.util_functions import (
    get_commodity_types,
    get_commodities_by_type,
)

from utils.data_fetching import fetch_commodity_info

# Configure the page
st.set_page_config(
    page_title="Commodify",
    page_icon="🚀",
)

#####Sidebar Start#####

# Add a new section for selecting commodity type
st.sidebar.markdown("## **Select Domain**")
commodity_types = get_commodity_types()

# Add a radio button for selecting the type
selected_type = st.sidebar.radio(
    "Select One",
    commodity_types,
)

# Fetch and store commodity data
commodity_dict = get_commodities_by_type(selected_type)

# Add a new section for selecting commodity type
st.sidebar.markdown("## **Select Commodity**")
# Add a dropdown for selecting the commodity
commodity = st.sidebar.selectbox(
    "Select One",
    list(commodity_dict.keys()),
)

# Build the commodity ticker
commodity_ticker = commodity_dict[commodity]


#####Sidebar End#####


# Fetch the info of the commodity
try:
    commodity_data_info = fetch_commodity_info(commodity_ticker)
except:
    st.error("Error: Unable to fetch the commodity data. Please try again later.")
    st.stop()


#####Title#####

# Add title to the app
st.markdown("# **Commodity Analysis Plus**")

# Add a subtitle to the app
st.markdown("##### **Enhancing Your Commodity Market Insights**")

#####Title End#####


#####Basic Information#####

# Add a heading
st.markdown("## **Basic Information**")

# Create 2 columns
col1, col2 = st.columns(2)

# Row 1
col1.dataframe(
    pd.DataFrame(
        {"Short Name": [commodity_data_info["Basic Information"]["shortName"]]}
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame({"Symbol": [commodity_data_info["Basic Information"]["symbol"]]}),
    hide_index=True,
    width=500,
)

# Row 2
col1.dataframe(
    pd.DataFrame(
        {
            "Underlying Symbol": [
                commodity_data_info["Basic Information"]["underlyingSymbol"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame(
        {"Quote Type": [commodity_data_info["Basic Information"]["quoteType"]]}
    ),
    hide_index=True,
    width=500,
)

# Create 3 columns
col1, col2, col3 = st.columns(3)
# Row 3
col1.dataframe(
    pd.DataFrame({"Currency": [commodity_data_info["Basic Information"]["currency"]]}),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame({"Exchange": [commodity_data_info["Basic Information"]["exchange"]]}),
    hide_index=True,
    width=500,
)
col3.dataframe(
    pd.DataFrame(
        {"Time Zone": [commodity_data_info["Basic Information"]["timeZoneShortName"]]}
    ),
    hide_index=True,
    width=500,
)

#####Price Information#####

# Add a heading
st.markdown("## **Price Information**")

# Create 2 columns
col1, col2 = st.columns(2)

# Row 1
col1.dataframe(
    pd.DataFrame(
        {"Previous Close": [commodity_data_info["Price Information"]["previousClose"]]}
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame({"Open": [commodity_data_info["Price Information"]["open"]]}),
    hide_index=True,
    width=500,
)

# Row 2
col1.dataframe(
    pd.DataFrame({"Day Low": [commodity_data_info["Price Information"]["dayLow"]]}),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame({"Day High": [commodity_data_info["Price Information"]["dayHigh"]]}),
    hide_index=True,
    width=500,
)

# Row 3
col1.dataframe(
    pd.DataFrame(
        {
            "Regular Market Previous Close": [
                commodity_data_info["Price Information"]["regularMarketPreviousClose"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame(
        {
            "Regular Market Open": [
                commodity_data_info["Price Information"]["regularMarketOpen"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)

# Row 4
col1.dataframe(
    pd.DataFrame(
        {
            "Regular Market Day Low": [
                commodity_data_info["Price Information"]["regularMarketDayLow"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame(
        {
            "Regular Market Day High": [
                commodity_data_info["Price Information"]["regularMarketDayHigh"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)

#####Volume Information#####

# Add a heading
st.markdown("## **Volume Information**")

# Create 2 columns
col1, col2, col3 = st.columns(3)

# Row 1
col1.dataframe(
    pd.DataFrame({"Volume": [commodity_data_info["Volume Information"]["volume"]]}),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame(
        {
            "Regular Market Volume": [
                commodity_data_info["Volume Information"]["regularMarketVolume"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
col3.dataframe(
    pd.DataFrame(
        {"Average Volume": [commodity_data_info["Volume Information"]["averageVolume"]]}
    ),
    hide_index=True,
    width=500,
)

# Create 2 columns
col1, col2 = st.columns(2)
# Row 2
col1.dataframe(
    pd.DataFrame(
        {
            "Average Volume (10 Days)": [
                commodity_data_info["Volume Information"]["averageVolume10days"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)

# Row 3
col2.dataframe(
    pd.DataFrame(
        {
            "Average Daily Volume (10 Day)": [
                commodity_data_info["Volume Information"]["averageDailyVolume10Day"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)  # Placeholder for the second column

#####Bid-Ask Spread#####

# Add a heading
st.markdown("## **Bid-Ask Spread**")

# Create 2 columns
col1, col2 = st.columns(2)

# Row 1
col1.dataframe(
    pd.DataFrame({"Bid": [commodity_data_info["Bid-Ask Spread"]["bid"]]}),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame({"Ask": [commodity_data_info["Bid-Ask Spread"]["ask"]]}),
    hide_index=True,
    width=500,
)

# Row 2
col1.dataframe(
    pd.DataFrame({"Bid Size": [commodity_data_info["Bid-Ask Spread"]["bidSize"]]}),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame({"Ask Size": [commodity_data_info["Bid-Ask Spread"]["askSize"]]}),
    hide_index=True,
    width=500,
)

#####Historical and Benchmark Data#####

# Add a heading
st.markdown("## **Historical and Benchmark Data**")

# Create 2 columns
col1, col2 = st.columns(2)

# Row 1
col1.dataframe(
    pd.DataFrame(
        {
            "52 Week Low": [
                commodity_data_info["Historical and Benchmark Data"]["fiftyTwoWeekLow"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame(
        {
            "52 Week High": [
                commodity_data_info["Historical and Benchmark Data"]["fiftyTwoWeekHigh"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)

# Row 2
col1.dataframe(
    pd.DataFrame(
        {
            "50 Day Average": [
                commodity_data_info["Historical and Benchmark Data"]["fiftyDayAverage"]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
col2.dataframe(
    pd.DataFrame(
        {
            "200 Day Average": [
                commodity_data_info["Historical and Benchmark Data"][
                    "twoHundredDayAverage"
                ]
            ]
        }
    ),
    hide_index=True,
    width=500,
)
