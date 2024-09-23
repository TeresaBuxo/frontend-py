import reflex as rx
from ..components.upload import upload_image
from ..components.input_text import SimpleTextInput
from .forms import ProjectForm,InstitutionForm, VideoForm

project_form = ProjectForm.create
instittution_form = InstitutionForm.create
video_form = VideoForm.create

def add_new_popover(my_title:str) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.icon_button("square-plus", size="3")),
        rx.dialog.content(
            rx.dialog.title(f"Add new {my_title}"),
            rx.dialog.description(
                f"Add new {my_title} details",
                size="2",
                margin_bottom="16px",
            ),
            rx.match(
                my_title,
                ("project", project_form()),
                ("institution", instittution_form()),
                ("video",video_form()),
                ("device", instittution_form()),
                instittution_form(),
                ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancel",
                        color_scheme="gray",
                        variant="soft",
                    ),
                ),
                rx.dialog.close(
                    rx.button("Save"),
                    type ='submit',
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
    )