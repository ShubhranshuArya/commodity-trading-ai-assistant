import streamlit as st
from datetime import datetime, timedelta

from utils.util_functions import get_stock_news_topics


# Configure the page
st.set_page_config(
    page_title="Commodify",
    page_icon="🚀",
)

#####Sidebar Start#####

#####Sidebar End#####


#####Title#####

# Title
st.markdown("# **🎲 Stock Sentiment Analysis**")

# Subtitle
st.markdown("##### **Analyze market sentiment from news data**")

#####Title End#####


#####Main Section Start#####

st.markdown("### **Stock**")
# Stock selection
stock_symbol = st.selectbox(
    "Select Stock",
    ["AAPL", "GOOGL", "MSFT", "AMZN", "META"],
    index=0,
    label_visibility="collapsed",
)

st.markdown("### **News Topics**")
# News topics selection
news_topics = get_stock_news_topics()
topics = st.multiselect(
    "Select News Topics",
    list(news_topics.keys()),
    default=["All"],
    label_visibility="collapsed",
)

# Analysis button
analyze_button = st.button(
    "Analyze Sentiment", type="primary", use_container_width=True
)

# If analyze button is clicked, show results
if analyze_button:
    st.markdown("---")

    # Show loading spinner while "analyzing"
    with st.spinner("Calculating the Sentiment..."):
        # Placeholder for sentiment score (replace with actual analysis)
        sentiment_score = 0.65

        # Display results in columns
        res_col1, res_col2 = st.columns([2, 1])

        with res_col1:
            st.markdown("### Sentiment Analysis Results")

        with res_col2:
            st.markdown("### Summary")
            st.markdown(
                f"**Overall Sentiment:** {'Positive' if sentiment_score > 0.3 else 'Neutral' if sentiment_score > -0.3 else 'Negative'}"
            )
            st.markdown(f"**Confidence Score:** {abs(sentiment_score):.2f}")

    # Chat interface
    st.markdown("---")
    st.markdown("### Ask Questions About the Analysis")
    user_question = st.text_input(
        "Enter your question:",
        placeholder="E.g., Why is the sentiment positive for this stock?",
    )

    if user_question:
        st.markdown(
            "**AI Assistant:** This is a placeholder response. In a real implementation, this would be connected to an AI model that can analyze the sentiment data and provide detailed answers to user questions."
        )

#####Main Section End#####
