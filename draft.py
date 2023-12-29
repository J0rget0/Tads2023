
import plotly.express as px
from Data.download import download_data

data = download_data('BBAS3.SA')

px.line(
    data.reset_index(),
    x='Date', y=['Close', 'SMA', 'LMA'], 
    title=ticker,
    title = 'BBAS3',
    labels = {'Close': 'Fechamento', 'Date': 'Data'},
    color_discrete_map={'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
)

from plot.interactive import plot_line_i
plot_line_i('BBAS3.SA')