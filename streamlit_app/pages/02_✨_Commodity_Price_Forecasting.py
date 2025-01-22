# Imports
import plotly.graph_objects as go
import streamlit as st
import pandas as pd

from utils.util_functions import (
    get_commodity_types,
    get_commodities_by_type,
    get_period_intervals,
    get_prediction_strategies,
    get_backtesting_timeframes,
)

from utils.data_fetching import fetch_commodity_history

from utils.forecast_compute import commodity_forecast_backtesting

# Configure the page
st.set_page_config(
    page_title="Commodify",
    page_icon="🚀",
)


#####Sidebar Start#####

# Add a new section for selecting commodity type
st.sidebar.markdown("## **Sector**")
commodity_types = get_commodity_types()

# Add a radio button for selecting the type
selected_type = st.sidebar.radio(
    "Select One",
    commodity_types,
)

# Fetch and store commodity data
commodity_dict = get_commodities_by_type(selected_type)

# Add a new section for selecting commodity type
st.sidebar.markdown("## **Commodity**")
# Add a dropdown for selecting the commodity
commodity = st.sidebar.selectbox(
    "Select One",
    list(commodity_dict.keys()),
)

# Build the commodity ticker
commodity_ticker = commodity_dict[commodity]

# Fetch and store periods and intervals
periods = get_period_intervals()

# Add a selector for period
period = st.sidebar.selectbox("Choose historical period", list(periods.keys()))

# Add a selector for interval
interval = st.sidebar.selectbox("Choose historical interval", periods[period])

# Add a radio for strategy selection
st.sidebar.markdown("## **Forecasting Strategy**")
strategy_types = get_prediction_strategies()
selected_strategy = st.sidebar.radio(
    "Select One",
    strategy_types,
)

backtesting_timeframes = get_backtesting_timeframes()
# Add a selector for backtesting timeframe
st.sidebar.markdown("## **Backtesting Forecast Timeframe**")
backtesting_timeframe = st.sidebar.selectbox(
    "Select timeframe", list(backtesting_timeframes.keys())
)


#####Sidebar End#####


#####Title#####

# Add title to the app
st.markdown("# **Commodity Price Forecasting**")

# Add a subtitle to the app
st.markdown(
    "##### **Enhance Investment Decisions in Commodities through Data-Driven Forecasting**"
)

#####Title End#####


# Fetch the commodity historical data
commodity_data = fetch_commodity_history(commodity_ticker, period, interval)


#####Historical Data Graph#####

# Add a title to the historical data graph
st.markdown("### **Historical Data**")

# Create a plot for the historical data
fig = go.Figure(
    data=[
        go.Candlestick(
            x=commodity_data.index,
            open=commodity_data["Open"],
            high=commodity_data["High"],
            low=commodity_data["Low"],
            close=commodity_data["Close"],
        )
    ]
)

# Customize the historical data graph
fig.update_layout(xaxis_rangeslider_visible=False)

# Use the native streamlit theme.
st.plotly_chart(fig, use_container_width=True)

#####Historical Data Graph End#####

#####Backtesting Prediction Strategy Graph#####

# Unpack the data
original_values, backtested_values = commodity_forecast_backtesting(
    commodity_ticker,
    backtesting_timeframes[backtesting_timeframe],
    # strategy_types[selected_strategy],
)

# Check if the data is not None
if original_values is not None and (backtested_values >= 0).all():
    st.markdown("### **Forecasting Strategy Analysis with Backtesting**")

    # Create a plotly figure
    comparison_fig = go.Figure()

    # Add original values to the plot
    comparison_fig.add_trace(
        go.Scatter(
            x=original_values.index,
            y=original_values["Close"],
            mode="lines",
            name="Original Value",
            line=dict(color="grey"),
        )
    )

    # Add backtested values to the plot
    comparison_fig.add_trace(
        go.Scatter(
            x=backtested_values.index,
            y=backtested_values,
            mode="lines",
            name="Forecasted Value",
            line=dict(color="yellow"),
        )
    )

    # Display the comparison plot
    st.plotly_chart(comparison_fig, use_container_width=True)
    #####Overlay Comparison Graph End#####

# If the data is None
else:
    # Add a title to the Commodity Price prediction graph
    st.markdown("## **Backtesting Prediction Strategy**")

    # Add a message to the Commodity Price prediction graph
    st.markdown("### **Backtesting not enabled**")

#####Commodity Price Prediction Graph End#####
