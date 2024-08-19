import reflex as rx 

from .platform_base import platform_base
from ..constants import urls
from ..components.project_card import project_card

@rx.page(route=urls.PROJECTS_URL)
def platform_page() -> rx.Component:
    my_child = rx.vstack(
                rx.heading('Projects', size="9"),
                rx.text(
                    'Discover the different projects',
                ),
                rx.grid(
                    project_card('/logo1.png','Care Again','descirption',urls.HOME_URL),
                    project_card('/incubator.jpeg','In3ator','La incubadora de código abierto y bajo coste','https://medicalopenworld.org/'),
                    project_card('/logo1.png','Care Again','descirption',urls.HOME_URL),
                    project_card('/logo1.png','Care Again','descirption',urls.HOME_URL),
                    project_card('/logo1.png','Care Again','descirption',urls.HOME_URL),
                    flow="row",
                    columns="1",
                    spacing_y="4",
                    width="100%",
                    align ="start"
                ),
                spacing="5",
                justify="left",
                align="left",
                height="100%",
                id='my-child'
            )
    return platform_base(my_child)