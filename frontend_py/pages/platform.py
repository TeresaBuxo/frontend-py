import reflex as rx 

from .platform_base import platform_base
from ..navigation import urls

@rx.page(route=urls.PLATFORM_URL)
def platform_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "Something cool about us.",
            ),
            spacing="5",
            justify="center",
            align="center",
            height="75vw",
            id='my-child'
        )
    return platform_base(my_child)