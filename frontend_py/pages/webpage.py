import reflex as rx 

from .webpage_base import base_page
from ..constants import urls
from ..components.map import map_location

def home_logo() -> rx.Component:
    return rx.vstack(
        rx.heading("Bienvenido a Care Again",size="8",color="gray",high_contrast=True,),
        rx.image('full_logo.png', width="50%",),
        rx.heading("La plataforma para facilitar el acceso a tecnología médica",size="8",color="gray",high_contrast=True,align="centre"),    
        margin="12px",
        width="100%",
        border="10px",
        align="center",
        justify="center",
        id="home_logo",
    )

def problem_section() -> rx.Component:
    return rx.hstack(
                rx.image('hombre_repadando_equipos.webp',
                        width='40%',
                        align="start"),

                rx.vstack(
                    rx.heading("El problema", size="9",align = "center"),
                    rx.blockquote("Escasez de equipos médicos en comunidades vulnerables."),
                    rx.blockquote("Dificultad para donar equipos médicos de manera eficiente."),
                    rx.blockquote("Falta de acceso a diseños de dispositivos médicos de bajo costo y fáciles de construir."),
                    spacing="5",
                    justify="center",
                    align="start",
                    min_height="60vh",
                ),
                width="100%",
                bg=rx.color("teal", 2),
                id="problem_section"
            )

def solution_section() ->rx.Component:
    return rx.hstack(
                rx.vstack(
                    #rx.heading("Nuestra solución", size="9",align = "center"),
                    rx.text(
                        "Desde Care Again proponemos crear un repositorio y plataforma colaborativa donde se desarrollen y compartan planos y guías para la construcción de dispositivos médicos con materiales accesibles. ",
                        size="5"),
                    rx.blockquote("Nuestra visión", size="7", align="start"),
                    rx.text("El objetivo de facilitar el acceso a equipos médicos esenciales a nivel global a través de una plataforma gratuita donde compartir proyectos open source para la construcción local de equipos médicos.",
                        size="5"),
                    rx.blockquote("Nuestra misión", size="7"),
                    rx.text("Conectar a equipos de desarrollo con creadores locales de equipos médicos y proporcionar recursos y diseños open source para que las comunidades puedan construir sus propios dispositivos médicos.",
                        size="5"),
                    spacing="5",
                    justify="center",
                    min_height="85vh",
                    padding="15px",
                    margin="100px"
                ),
                rx.image('padre_hijo_reparando.png',
                        width='40%',
                        align="end",
                        justify="end"),
                id="solution_section"
            )

def community_section() -> rx.Component:
    return rx.vstack(
        rx.heading("Hazlo possible! Únete a la comunidad!",size="9"),
        map_location(),
        align="center",
        bg=rx.color("teal", 2),
        spacing="5",
        padding="1%",
        color_scheme="teal",
        width="100%",
        id="community_section",
    )

def contact_section() ->rx.Component:
    return rx.hstack(
        rx.image("cor_nobackground.png"),
        rx.vstack(
            rx.heading("Contacta con nosotros",size="9"),
            rx.hstack(
                rx.icon("mail"),
                rx.text(urls.EMAIL)
            ),
            rx.hstack(
                rx.icon("message-circle"),
                rx.text(urls.EMAIL)
            ),
            align="center",
            justify="center",
            padding="5%",
            spacing="5",
        ),
        width="100%",
        align="center",
        color_scheme="teal",
        margin="15px",
        padding="15px",
        id="contact_section"
    )

@rx.page(route=urls.HOME_URL, title = 'Home')
def home_page() -> rx.Component:
    my_child = rx.box(
    rx.desktop_only(
        rx.vstack(
            rx.image("ai_hospital_pregnant.png",width="100%"),
            home_logo(),
            problem_section(),
            solution_section(),
            community_section(),
            contact_section(),
            align="center"
        )
    ),
    rx.mobile_and_tablet(
        rx.vstack(
            rx.image("ai_hospital_pregnant.png",width="100%"),
            home_logo(),
            problem_section(),
            solution_section(),
            community_section(),
            contact_section(),
        ),
        id="box-home"
    )
    )
    return base_page(my_child)