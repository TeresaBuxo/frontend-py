import reflex as rx 

from .base import base_page
from ..constants import urls
from ..components.login_card import login_multiple_thirdparty

@rx.page(route=urls.LOGIN_URL)
def login_page() -> rx.Component:
    my_child = rx.center(
                    login_multiple_thirdparty(),
                    spacing="5",
                    justify="center",
                    align="center",
                    min_height="70vh",
                    id='my-child',
                )
    return base_page(my_child)