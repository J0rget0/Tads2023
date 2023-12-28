import plotly.express as px
from data.download import download_data


    labels={'Close': 'Fechamento', 'Date': 'Data'},
    color_discrete_map={'Close': 'black', 'SMA': 'blue', 'LMA': 'red'}
)


from plot.interactive import plot_line_i

plot_line_i('CPLE3.SA')
