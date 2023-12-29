import plotly.express as px
from Data.download import download_data

def plot_line_i(ticker:str):
    """ Plot an interactive plot using plotly.

    Args:
        ticker (str): The ticker of financial asset.

    Returns:
        plotly: A ticker plot.
    """

    data = download_data(ticker)

    fig = px.line(
        data.reset_index(),
        x = 'Date', y = ['Close', 'SMA', 'LMA'], title = ticker,
        labels = {'Close': 'Fechamento', 'Date': 'Data'},
        color_discrete_map={'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
    )

    return fig