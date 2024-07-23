import plotly.graph_objects as go
import reflex as rx

def map_location():

    fig = go.Figure(go.Scattermapbox())

    fig.update_layout(
        mapbox = {'style': "open-street-map", 'center': {'lon': 30, 'lat': 30}, 'zoom': 1},
        showlegend = False,
        margin = {'l':0, 'r':0, 'b':0, 't':0})

    return rx.center(
                rx.plotly(data=fig),
                height="100%",
                width="100%",
                justify="centre",
                id="box-map",
            )