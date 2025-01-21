import streamlit as st

st.set_page_config(
    page_title="Commodify",
    page_icon="🚀",
)

st.markdown(
    """# 🚀 **Commodify**
### **AI Powered Commodity Trading**

**Commodify is an AI tool for commodity trading and risk management in real-time. It utilizes multiple machine learning models for time series forecasting to forecast commodity prices and help investors make data-driven decisions.**

## 🏗️ **How It's Built**

Commodify is built with these core frameworks and modules:

- **Streamlit** - To create the web app UI and interactivity 
- **YFinance** - To fetch real-time commodity data from Yahoo Finance API
- **StatsModels** - To build the ARIMA time series forecasting model
- **Plotly** - To create interactive financial charts

The app workflow is:

1. User selects a commodity
2. Historical data is fetched with YFinance
3. ARIMA model is trained on the data 
4. Model makes multi-day price forecasts
5. Results are plotted with Plotly

## 🎯 **Key Features**

- **Real-time data** - Fetch latest prices and fundamentals 
- **Financial charts** - Interactive historical and forecast charts
- **ARIMA forecasting** - Make statistically robust predictions
- **Backtesting** - Evaluate model performance
- **Responsive design** - Works on all devices

## 📈 **Future Roadmap**

Some potential features for future releases:

- **More advanced forecasting models like LSTM**
- **Quantitative trading strategies**
- **Portfolio optimization and tracking**
- **Additional fundamental data**
- **User account system**

## **⚖️ Disclaimer**
**This project is under construction and is not intended for production use.**
"""
)
