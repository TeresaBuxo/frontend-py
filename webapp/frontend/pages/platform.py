import reflex as rx
from .platform_base import platform_base
from ..constants import urls
from ..components.project_card import project_grid_horizontal
from ..components.question_card import question_grid_vertical
from ..states.project_state import ProjectState
from ..states.question_state import QuestionState
from ..states.auth_state import AuthState

def section_title(section_icon:str,section_title:str, section_link:str) -> rx.Component(): # type: ignore
    return rx.hstack(
        rx.icon(section_icon,color = "teal"),
        rx.heading(section_title,size="5", color = "teal"),
        rx.link(f"Go to {section_title}",href=section_link),
        spacing = "5",
        color = "accent"
    )

@rx.page(route=urls.PLATFORM_URL, 
         on_load= [ProjectState.get_list_projects, QuestionState.get_list_questions])
def platform_home() -> rx.Component:
    home = rx.vstack(
                rx.heading('Most recent', size="5"),
                section_title("square-library",'Projects', urls.PROJECTS_URL),
                project_grid_horizontal(),
                section_title("square-play",'Videos', urls.VIDEOS_URL),
                # section_title("store",'Market', urls.PLATFORM_URL),
                section_title('file-question',"Questions", urls.QUESTIONS_URL),
                question_grid_vertical(),
                align = "start",
                justify="start",
                width ="100%"
    )
    return platform_base(home)