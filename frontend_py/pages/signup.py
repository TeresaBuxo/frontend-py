import reflex as rx 

from .base import base_page
from ..navigation import urls
from ..components.signup_card import signup_multiple_thirdparty

@rx.page(route=urls.SIGNUP_URL)
def signup_page() -> rx.Component:
    my_child = rx.center(
                    signup_multiple_thirdparty(),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="70vh",
                    id='my-child',
                )
    return base_page(my_child)