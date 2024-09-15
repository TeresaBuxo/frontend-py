import reflex as rx

def add_new_popover() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(rx.icon_button("square-plus", size="3")),
        rx.dialog.content(
            rx.dialog.title("Add new"),
            rx.dialog.description(
                "Add new whatever",
                size="2",
                margin_bottom="16px",
            ),
            rx.flex(
                rx.text(
                    "Name",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    default_value="Freja Johnson",
                    placeholder="Enter name",
                ),
                rx.text(
                    "Email",
                    as_="div",
                    size="2",
                    margin_bottom="4px",
                    weight="bold",
                ),
                rx.input(
                    default_value="freja@example.com",
                    placeholder="Enter your email",
                ),
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
                ),
                spacing="3",
                margin_top="16px",
                justify="end",
            ),
        ),
    )