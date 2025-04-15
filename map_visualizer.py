
import plotly.express as px

def plot_routes(df):
    fig = px.scatter_geo(df, lat='lat', lon='lon', color='origin',
                         hover_name='destination', size='delay_minutes',
                         projection='natural earth')
    return fig
