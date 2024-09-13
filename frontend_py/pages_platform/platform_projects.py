import reflex as rx 

from .platform_base import platform_base
from ..constants import urls
from ..components.project_card import project_card,project_grid
from ..states.project_state import ProjectState

@rx.page(route=urls.PROJECTS_URL, on_load= ProjectState.get_list_projects)
def platform_page() -> rx.Component:
    my_child = rx.vstack(
                rx.heading('Projects', size="9"),
                rx.text(
                    'Discover the different projects',
                ),
                project_grid(),
                align = "start",
                justify="start",
    )
    return platform_base(my_child)