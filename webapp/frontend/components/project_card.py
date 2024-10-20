import reflex as rx
import httpx
from ..states.project_state import ProjectState

def project_card_vertical(image: str, project_title: str, project_description: str, project_link: str,group_logo:str)-> rx.Component:

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

def project_grid_vertical()-> rx.Component:
    return rx.vstack(
        rx.cond(
            ProjectState.projects != [],
            rx.foreach(ProjectState.projects, lambda value, i: 
                        project_card_vertical(image = '/' + value["image"],
                                    project_title = value["project_name"],
                                    project_description = value["description"],
                                    project_link = value["link"],
                                    group_logo = "logo1.png")),
            rx.text("No projects available")
        ),   
        spacing_y="4",
        #width="100%",
        align ="start",
        justify = "start"
    )

def project_card_horizontal(image: str, project_title: str, project_description: str, project_link: str,group_logo:str)-> rx.Component:

    return rx.container(
        rx.card(
            rx.link(
                rx.flex(
                    rx.image(src=image,
                            width="140px",
                            height="140px"),
                    rx.box(
                        # rx.image(src=group_logo,
                        #     height="40px",
                        #     align="right"),
                        rx.heading(project_title),
                        # rx.text(project_description),
                        width="100%",
                        spacing="2",
                        padding ="0",
                        align="center"
                    ),
                    spacing="2",
                    direction="column",
                    padding ="0",
                    align="center"
                ),
                href= project_link
            ),
            as_child=True,
            size="5",
            height='20vw',
            padding ="10%",
            align="center"
        ),
        height = 'auto',
        width = '20vw',
        align='start',

    )

def project_grid_horizontal()-> rx.Component:
    return rx.hstack(
        rx.cond(
            ProjectState.projects != [],
            rx.foreach(ProjectState.projects, lambda value, i: 
                        project_card_horizontal(image = '/' + value["image"],
                                    project_title = value["project_name"],
                                    project_description = value["description"],
                                    project_link = value["link"],
                                    group_logo = "logo1.png")),
            rx.text("No projects available")
        ),   
        spacing_y="4",
        #width="100%",
        align ="start",
        justify = "start"
    )