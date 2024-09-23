import plotly.graph_objects as go
import reflex as rx

def map_location():

    fig = go.Figure(go.Scattermapbox())

    fig.update_layout(
        mapbox = {'style': "open-street-map", 'center': {'lon': 30, 'lat': 30}, 'zoom': 1},
        showlegend = False,
        margin = {'l':0, 'r':0, 'b':0, 't':0})

    return rx.fragment(
                rx.plotly(data=fig,
                    width="90%",
                    height="80h"
                ),
                height="80hv",
                width="100%",
                id="box-map",
            )