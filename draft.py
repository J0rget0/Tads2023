fix/draft
import plotly.express as px
from data.download import download_data

data = download_data('BBAS3.SA')
data[['Close']]
data ['SMA']= data ['Close'].rolling(window = 9).mean()
data ['LMA']= data ['Close'].rolling(window = 72).mean()

import plotly.express as px

px.line(
    data.reset_index(),
    x='Date', y=['Close', 'SMA', 'LMA'], title='BBAS3',
    labels={'Close': 'Fechamento', 'Date': 'Data'},
    color_discrete_map={'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
)


from plot.interactive import plot_line_i

plot_line_i('CPLE3.SA')
