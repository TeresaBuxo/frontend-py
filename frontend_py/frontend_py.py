"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .pages import home,about,contact,community,login,signup,platform
from .navigation import urls
from rxconfig import config


class State(rx.State):
    """The app state."""
    label = "hola!"

    def handle_input_change(self,val):
        self.label = val

    ...


app = rx.App(
    theme=rx.theme(
        appearance="dark", 
        has_background=True, 
        panel_background="solid",
        scaling="90%",
        radius="medium", 
        accent_color="teal"
    )
)
