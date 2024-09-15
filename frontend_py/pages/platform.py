import reflex as rx
from .platform_base import platform_base
from ..constants import urls
from ..components.project_card import project_card,project_grid
from ..states.project_state import ProjectState
from ..states.auth_state import AuthState

def section_title(section_icon:str,section_title:str, section_link:str) -> rx.Component(): # type: ignore
    return rx.hstack(
        rx.icon(section_icon,color = "teal"),
        rx.heading(section_title,size="5", color = "teal"),
        rx.link(f"Go to {section_title}",href=section_link),
        spacing = "5",
        color = "accent"
    )

@rx.page(route=urls.PLATFORM_URL)#, on_load= ProjectState.get_list_projects)
def platform_home() -> rx.Component:
    home = rx.vstack(
                rx.heading('Most recent', size="5"),
                section_title("square-library",'Projects', urls.PROJECTS_URL),
                section_title("square-play",'Videos', urls.PROJECTS_URL),
                #project_grid(),
                align = "start",
                justify="start",
                width ="100%"
    )
    return platform_base(home)