import plotly.express as px
from data.download import download_data

def plot_line_i(ticker: str):
    """ Plot an interactive plot using plotly.

    Args:
        ticker (str): The ticker of the financial asset.

    Returns:
        plotly: A ticker plot.
    """

    # Download data for the specified ticker
    data = download_data(ticker)
    
    # Calculate moving averages
    data['SMA'] = data['Close'].rolling(window=9).mean()
    data['LMA'] = data['Close'].rolling(window=72).mean()

    # Create an interactive line plot
    fig = px.line(
        data.reset_index(),
        x='Date', y='Close',
        title=ticker,
        labels={'Close': 'Fechamento', 'Date': 'Data'},
        color_discrete_map={'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
    )

    return fig
