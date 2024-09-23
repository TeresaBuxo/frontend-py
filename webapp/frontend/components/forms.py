import reflex as rx
from typing import List
from .input_text import SimpleTextInput
from .upload import upload_image

class ProjectForm(rx.ComponentState):
    # Define form state variables
    name: str = ""
    link: str = ""
    description: str = ""
    uploaded_img: str = ""

    @classmethod
    def set_name(cls, value: str):
        cls.name = value

    @classmethod
    def set_link(cls, value: str):
        cls.link = value
    
    @classmethod
    def set_description(cls, value: str):
        cls.description = value

    @classmethod
    def handle_submit(cls):

        # Handle form submission (e.g., print or send data)
        print(f"Form submitted with Name: {cls.name}, Email: {cls.name}")

    @classmethod
    def get_component(cls, **props):
        return rx.dialog.root(
        rx.dialog.trigger(rx.icon_button("square-plus", size="3")),
        rx.dialog.content(
            rx.dialog.title(f"Add new Project"),
            rx.dialog.description(
                f"Add new Project details",
                size="2",
                margin_bottom="16px",
            ),
            rx.form(
                rx.flex(
                    SimpleTextInput.create(
                        title="Name",
                        placeholder="Enter your Name",
                        value=cls.name,
                        on_change=cls.set_name,
                    ),
                    SimpleTextInput.create(
                        title="Link to website",
                        placeholder="Enter your Link to website",
                        value=cls.link,
                        on_change=cls.set_link,
                    ),
                    SimpleTextInput.create(
                        title="Project Description",
                        placeholder="Enter your Project Description",
                        value=cls.description,
                        on_change=cls.set_description,
                    ),
                    upload_image("Image"),
                    direction="column",
                    spacing="3",
                ),
                width="100%"
                # on_submit=cls.handle_submit,
                # reset_on_submit=True,
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
                        # on_click=cls.handle_submit,
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
            ),
        )



class InstitutionForm(rx.ComponentState):
    # Define form state variables
    name: str = ""
    address: str = ""
    type: str = ""
    uploaded_img: str = ""
    map_visible: bool = True
    all_institution: list[str] = ["Hospital","Intermediate NGO","University","Organization"]

    @classmethod
    def set_name(cls, value: str):
        cls.name = value
    
    @classmethod
    def set_type(cls, value: str):
        cls.type = value

    @classmethod
    def set_address(cls, value: str):
        cls.address = value

    @classmethod
    def handle_submit(cls):
        # Handle form submission (e.g., print or send data)
        print(f"Form submitted with Name: {cls.name}, Email: {cls.name}")

    @classmethod
    def get_component(cls, **props):
        return rx.dialog.root(
        rx.dialog.trigger(rx.icon_button("square-plus", size="3")),
        rx.dialog.content(
            rx.dialog.title(f"Add new Institution"),
            rx.dialog.description(
                f"Add new Institution details",
                size="2",
                margin_bottom="16px",
            ),
            rx.form(
            rx.flex(
                SimpleTextInput.create(
                    title="Name",
                    placeholder="Enter your Name",
                    value=cls.name,
                    on_change=cls.set_name,
                ),
                rx.select(cls.all_institution, 
                          placeholder="Selection of Fruits",
                          on_change=cls.set_type),
                SimpleTextInput.create(
                    title="Adress",
                    placeholder="Enter your Adress",
                    value=cls.address,
                    on_change=cls.set_address,
                ),
                upload_image("Image"),
                rx.flex(
                    rx.switch(default_checked=True),
                    rx.text("Appear in the community map"),
                    spacing="2",
                ),
                direction="column",
                spacing="3",
            ),
            width="100%"
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
                        # on_click=cls.handle_submit,
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
                width="100%",
                reset_on_submit=True,
        )
        )

    
class VideoForm(rx.ComponentState):
    # Define form state variables
    name: str = ""
    link: str = ""
    description: str = ""
    uploaded_img: str = ""

    @classmethod
    def set_name(cls, value: str):
        cls.name = value

    @classmethod
    def set_link(cls, value: str):
        cls.link = value
    
    @classmethod
    def set_description(cls, value: str):
        cls.description = value

    @classmethod
    def handle_submit(cls):
        # Handle form submission (e.g., print or send data)
        print(f"Form submitted with Name: {cls.name}, Email: {cls.name}")

    @classmethod
    def get_component(cls, **props):
        return rx.dialog.root(
        rx.dialog.trigger(rx.icon_button("square-plus", size="3")),
        rx.dialog.content(
            rx.dialog.title(f"Add new Video"),
            rx.dialog.description(
                f"Add new video details",
                size="2",
                margin_bottom="16px",
            ),
            rx.form(
                rx.flex(
                    SimpleTextInput.create(
                        title="Name",
                        placeholder="Enter your Name",
                        value=cls.name,
                        on_change=cls.set_name,
                    ),
                    SimpleTextInput.create(
                        title="Link to youtube video",
                        placeholder="Enter your youtube video",
                        value=cls.name,
                        on_change=cls.set_name,
                    ),
                    SimpleTextInput.create(
                        title="Video Description",
                        placeholder="Enter your Video Description",
                        value=cls.description,
                        on_change=cls.set_description,
                    ),
                    upload_image("Image"),

                    direction="column",
                    spacing="3",
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
                        # on_click=cls.handle_submit,
                    ),
                    spacing="3",
                    margin_top="16px",
                    justify="end",
                ),
                width="100%",
                reset_on_submit=True,
            ),
        )
        )