

def menu_item_link(text, href):
    return rx.menu.item(
        rx.link(
            text,
            href=href,
            width="100%",
            color="inherit",
        ),
        _hover={
            "color": styles.accent_color,
            "background_color": styles.accent_text_color,
        },
    )


def menu_button() -> rx.Component:
    """The menu button on the top right of the page.

    Returns:
        The menu button component.
    """
    from reflex.page import get_decorated_pages

    return rx.box(
        rx.menu.root(
            rx.menu.trigger(
                rx.button(
                    rx.icon("menu"),
                    variant="soft",
                )
            ),
            rx.menu.content(
                *[
                    menu_item_link(page["title"], page["route"])
                    for page in get_decorated_pages()
                ],
                rx.menu.separator(),
                menu_item_link("About", "https://github.com/reflex-dev"),
                menu_item_link("Contact", "mailto:founders@=reflex.dev"),
            ),
        ),
        position="fixed",
        right="2em",
        top="2em",
        z_index="500",
    )
