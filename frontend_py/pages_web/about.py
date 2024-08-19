import reflex as rx 

from .base import base_page
from ..constants import urls

@rx.page(route=urls.ABOUT_URL, title ='CareAgain | About')
def about_page() -> rx.Component:
    my_child = rx.vstack(
            rx.heading("About Us", size="9"),
            rx.text(
                "Something cool about us.",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id='my-child'
        )
    return base_page(my_child)