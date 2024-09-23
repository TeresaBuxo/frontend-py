import reflex as rx 

from .platform_base import platform_base
from ..constants import urls
from ..components.map import map_location
#from ..components.dropdown import selectors,SelectorsState

@rx.page(route=urls.COMMUNITY_PLATFORM)
def community_page() -> rx.Component:
    my_child = rx.vstack(
                    rx.heading("Community",size="9"), 
                    rx.text('Discover workplaces close to you'),
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
                        #selectors(),
                        width="100%",
                        spacing="9",
                        justify='between',
                        align_items="top",
                    ),
                    map_location(),
                    spacing="5",
                    justify="betweeen",
                    align="center",
                    align_items="top",
                    min_height="70vh",
                    weight="100%",
                    id='my-child',
                )
    return platform_base(my_child)