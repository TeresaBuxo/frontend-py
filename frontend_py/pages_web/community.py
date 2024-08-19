import reflex as rx 

from .base import base_page
from ..constants import urls
from ..components.map import map_location
from ..components.dropdown_filter import selectors,SelectorsState

@rx.page(route=urls.COMMUNITY_URL)
def community_page() -> rx.Component:
    my_child = rx.container(
                rx.vstack(
                    rx.flex(
                        rx.vstack(
                            rx.text("Search by address..."), 
                            rx.input(      
                                rx.input.slot(rx.icon("search")),
                                placeholder="Search...",
                                type="search",
                                size="2",
                            )
                        ),
                        selectors(),
                        width="100%",
                        spacing="9",
                        justify='between',
                        align_items="top",
                    ),
                    map_location(),
                ),
                spacing="5",
                justify="betweeen",
                align="center",
                align_items="top",
                min_height="70vh",
                id='my-child',
                )
    return base_page(my_child)