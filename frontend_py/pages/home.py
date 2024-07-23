import reflex as rx 

from .base import base_page
from ..navigation import urls

@rx.page(route=urls.HOME_URL)
def home_page() -> rx.Component:
    my_child = rx.box(
    rx.desktop_only(
        rx.hstack(
            rx.image('world_nobackground.png',
                    width='65vw'),
            rx.vstack(
                rx.heading("HOME Us", size="9",align = "center"),
                rx.text(
                    "Something cool about us.",
                ),
                spacing="5",
                justify="center",
                align="center",
                min_height="85vh",
                id='my-child'
            )
        )
    ),
    rx.mobile_and_tablet(
        rx.vstack(
            rx.image('world_nobackground.png',
                    width='65vw'),
            rx.vstack(
                rx.heading("HOME Us", size="9",align = "center"),
                rx.text(
                    "Something cool about us.",
                ),
                spacing="5",
                justify="center",
                align="center",
                min_height="85vh",
                id='my-child'
            )
        )
        ),
        id="box-home"
    )
    return base_page(my_child)