import plotly.graph_objects as go


def create_sentiment_gauge(sentiment_score):
    """
    Creates a semi-circular gauge chart for sentiment visualization
    Args:
        sentiment_score (float): Sentiment score between -1 and 1
    Returns:
        plotly figure object
    """
    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=sentiment_score,
            domain={"x": [0, 1], "y": [0, 1]},
            gauge={
                "axis": {"range": [-1, 1]},
                "bar": {"color": "darkblue"},
                "steps": [
                    {"range": [-1, -0.3], "color": "red"},
                    {"range": [-0.3, 0.3], "color": "gray"},
                    {"range": [0.3, 1], "color": "green"},
                ],
                "threshold": {
                    "line": {"color": "black", "width": 4},
                    "thickness": 0.75,
                    "value": sentiment_score,
                },
            },
        )
    )

    fig.update_layout(
        height=300, margin=dict(l=10, r=10, t=40, b=10), font={"size": 16}
    )
    return fig
