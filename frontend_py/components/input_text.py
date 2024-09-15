import reflex as rx
import typing as Callable

class EditableText(rx.ComponentState):
    text: str = "Click to edit"
    original_text: str
    editing: bool = False

    def start_editing(self, original_text: str):
        self.original_text = original_text
        self.editing = True

    def stop_editing(self):
        self.editing = False
        self.original_text = ""
        

    @classmethod
    def get_component(cls, **props):
        # Pop component-specific props with defaults before passing **props
        value = props.pop("value", cls.text)
        on_change = props.pop("on_change", cls.set_text)
        cursor = props.pop("cursor", "pointer")

        # Set the initial value of the State var.
        initial_value = props.pop("initial_value", None)
        if initial_value is not None:
            # Update the pydantic model to use the initial value as default.
            cls.__fields__["text"].default = initial_value

        # Form elements for editing, saving and reverting the text.
        edit_controls = rx.hstack(
            rx.input(
                value=value,
                on_change=on_change,
                **props,
            ),
            rx.icon_button(
                rx.icon("x"),
                on_click=[
                    on_change(cls.original_text),
                    cls.stop_editing,
                ],
                type="button",
                color_scheme="red",
            ),
            rx.icon_button(rx.icon("check")),
            align="center",
            width="100%",
        )

        # Return the text or the form based on the editing Var.
        return rx.cond(
            cls.editing,
            rx.form(
                edit_controls,
                on_submit=lambda _: cls.stop_editing(),
            ),
            rx.text(
                value,
                on_click=cls.start_editing(value),
                cursor=cursor,
                **props,
            ),
        )

# def input_text_editable(my_title:str,my_icon:str,my_placeholder:str,callback:Callable[[],None]) -> rx.Component:
#     return rx.vstack(
#                 rx.text(
#                     my_title,
#                     size="3",
#                     weight="medium",
#                     text_align="left",
#                     width="100%",
#                 ),
#                 rx.input(
#                     rx.input.slot(rx.icon(my_icon)),
#                     placeholder=my_placeholder,
#                     type="email",
#                     size="3",
#                     width="100%",
#                     on_change=callback,
#                 ),
#                 justify="start",
#                 spacing="2",
#                 width="100%",
#             )
