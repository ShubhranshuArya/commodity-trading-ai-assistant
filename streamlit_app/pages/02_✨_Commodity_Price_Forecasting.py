# Imports
import plotly.graph_objects as go
import streamlit as st

# Import helper functions
from helper import *

# Configure the page
st.set_page_config(
    page_title="Commodity Price Forecasting",
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

# Fetch and store periods and intervals
periods = fetch_periods_intervals()

# Add a selector for period
st.sidebar.markdown("## **Select period for historical data**")
period = st.sidebar.selectbox("Choose a period", list(periods.keys()))

# Add a selector for interval
st.sidebar.markdown("## **Select interval for historical data**")
interval = st.sidebar.selectbox("Choose an interval", periods[period])

timeframe = fetch_prediction_timeframe()

# Add a selector for timeframe
st.sidebar.markdown("## **Select Forecast Timeframe**")
forecast_timeframe = st.sidebar.selectbox(
    "Choose the timeframe", list(timeframe.keys())
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
st.markdown("## **Historical Data**")

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


#####Commodity Price Prediction Graph#####

# Unpack the data
train_df, test_df, forecast, predictions = generate_commodity_price_prediction(
    commodity_ticker,
    forecast_timeframe,
)

# Check if the data is not None
if train_df is not None and (forecast >= 0).all() and (predictions >= 0).all():
    # Add a title to the Commodity Price prediction graph
    st.markdown("## **Price Forecasting**")

    # Create a plot for the Commodity Price prediction
    fig = go.Figure(
        data=[
            go.Scatter(
                x=forecast.index,
                y=forecast,
                name="Forecast",
                mode="lines",
                line=dict(color="orange"),
            ),
        ]
    )

    # Customize the Commodity Price prediction graph
    fig.update_layout(xaxis_rangeslider_visible=False)

    # Use the native streamlit theme.
    st.plotly_chart(fig, use_container_width=True)

# If the data is None
else:
    # Add a title to the Commodity Price prediction graph
    st.markdown("## **Price Forecasting**")

    # Add a message to the Commodity Price prediction graph
    st.markdown("### **Data not enough for prediction.**")

#####Commodity Price Prediction Graph End#####
