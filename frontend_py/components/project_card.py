import reflex as rx
import httpx
from ..states.project_state import ProjectState

def project_card(image: str, project_title: str, project_description: str, project_link: str,group_logo:str)-> rx.Component:

    return rx.container(
        rx.card(
            rx.link(
                rx.flex(
                    rx.image(src=image,
                            width="120px",
                            height="120px"),
                    rx.box(
                        rx.image(src=group_logo,
                            height="40px",
                            align="right"),
                        rx.heading(project_title),
                        rx.text(
                            project_description
                        ),
                        width="100%",
                        spacing="5"
                    ),
                    spacing="2",
                    direction="row"
                ),
                href= project_link
            ),
            as_child=True,
            width = "100%",
            size="5",
        ),
        height = 'auto',
        #width = '100vw',
        align='start',

    )

def project_grid()-> rx.Component:
    return rx.vstack(
        rx.cond(
            ProjectState.projects != [],
            rx.foreach(ProjectState.projects, lambda value, i: 
                        project_card(image = '/' + value["image"],
                                    project_title = value["project_name"],
                                    project_description = value["description"],
                                    project_link = value["link"],
                                    group_logo = "logo01.png")),
            rx.text("No projects available")
        ),   
        spacing_y="4",
        #width="100%",
        align ="start",
        justify = "start"
    )