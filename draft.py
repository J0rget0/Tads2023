import plotly.express as px
from data.download import download_data


ticker = 'BBAS3.SA'

data = download_data(ticker)

data["SMA"] = data['Close'].rolling(window=9).mean()
data["LMA"] = data['Close'].rolling(window=72).mean()

px.line(
    data.reset_index(),
    x='Date', y=['Close', 'SMA', 'LMA'], title=ticker,
    labels={'Close': 'Fechamento', 'Date': 'Data'},
    color_discrete_map={'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
)


from plot.interactive import plot_line_i

plot_line_i('CPLE3.SA')
