import reflex as rx

def project_card(logo: str, project_title: str, project_description: str, project_link: str)-> rx.Component:
    return rx.container(
        rx.card(
            rx.link(
                rx.flex(
                    rx.image(src=logo,
                            width="120px",
                            height="120px"),
                    rx.box(
                        rx.heading(project_title),
                        rx.text(
                            project_description
                        ),
                    ),
                    spacing="2",
                ),
                href= project_link
            ),
            as_child=True,
            width = "100%",
            size="5",
        ),
        height = 'auto',
        width = '100vw',
        align='start',

    )