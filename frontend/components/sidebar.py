import reflex as rx

def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("anccent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_item(
    text: str, icon: str, href: str
) -> rx.Component:
    """Sidebar item.

    Args:
        text: The text of the item.
        url: The URL of the item.

    Returns:
        rx.Component: The sidebar item component.
    """
    # # Whether the item is active.
    # active = (rx.State.router.page.path == url.lower()) | (
    #     (rx.State.router.page.path == "/") & text == "Home"
    # )

    return rx.link(
        rx.hstack(
            rx.icon(icon),
            rx.text(text, size="4"),
            width="100%",
            padding_x="0.5rem",
            padding_y="0.75rem",
            align="center",
            style={
                "_hover": {
                    "bg": rx.color("accent", 4),
                    "color": rx.color("accent", 11),
                },
                "border-radius": "0.5em",
            },
        ),
        href=href,
        underline="none",
        weight="medium",
        width="100%",
    )


def sidebar_items() -> rx.Component:
    return rx.vstack(
        sidebar_item("Home", "code-xml", "/"),
        sidebar_item("Dashboard", "layout-dashboard", "/dashboard"),
        sidebar_item("Map", "map-pinned", "/#"),
        sidebar_item("Projects", "square-library", "/#"),
        sidebar_item("Analytics", "bar-chart-4", "/#"),
        sidebar_item("Messages", "mail", "/#"),
        spacing="1",
        width="100%",
    )

def sidebar_user_account(username: str, user_email:str) -> rx.Component:
    return rx.hstack(
            rx.icon_button(
                rx.icon("user"),
                size="3",
                radius="full",
            ),
            rx.vstack(
                rx.box(
                    rx.text(
                        username,
                        size="3",
                        weight="bold",
                    ),
                    rx.text(
                        user_email,
                        size="2",
                        weight="medium",
                    ),
                    width="100%",
                ),
                spacing="0",
                align="start",
                justify="start",
                width="100%",
            ),
            padding_x="0.5rem",
            align="center",
            justify="start",
            width="100%",
        )

def sidebar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.vstack(
                rx.hstack(
                    rx.image(
                        src="/logo1.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Care Again", size="7", weight="bold"
                    ),
                    align="center",
                    justify="start",
                    padding_x="0.5rem",
                    width="100%",
                ),
                sidebar_items(),
                rx.spacer(),
                rx.spacer(),
                rx.vstack(
                    rx.vstack(
                        sidebar_item(
                            "Settings", "settings", "/settings"
                        ),
                        sidebar_item(
                            "Log out", "log-out", "/#"
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    rx.divider(),
                    sidebar_user_account('My Account','email@gmail.com'),
                    width="100%",
                    spacing="5",

                ),
                spacing="5",
                # position="fixed",
                # left="0px",
                # z_index="5",
                padding_x="1em",
                padding_y="1.5em",
                bg=rx.color("jade", 3),
                top="auto",
                right="auto",
                height="100%",
                width="16em",
            ),
        ),
        rx.mobile_and_tablet(
            rx.drawer.root(
                rx.drawer.trigger(
                    rx.icon("align-justify", size=30)
                ),
                rx.drawer.overlay(z_index="5"),
                rx.drawer.portal(
                    rx.drawer.content(
                        
                        rx.vstack(
                            rx.vstack(
                                rx.box(
                                        rx.drawer.close(
                                            rx.icon("x", size=30)
                                        ),
                                        width="100%",
                                    ),
                                rx.hstack(
                                    rx.image(
                                        src="/logo1.png",
                                        width="2.25em",
                                        height="auto",
                                        border_radius="25%",
                                    ),
                                    rx.heading(
                                        "Care Again", size="7", weight="bold"
                                    ),
                                    align="center",
                                    justify="start",
                                    padding_x="0.5rem",
                                    width="100%",
                                ),
                                sidebar_items(),
                                rx.spacer(),
                                rx.vstack(
                                    rx.vstack(
                                        sidebar_item(
                                            "Settings",
                                            "settings",
                                            "/settings",
                                        ),
                                        sidebar_item(
                                            "Log out",
                                            "log-out",
                                            "/#",
                                        ),
                                        width="100%",
                                        spacing="1",
                                    ),
                                    rx.divider(margin="0"),
                                    sidebar_user_account('My Account','email@gmail.com'),
                                    width="100%",
                                    spacing="5",
                                ),
                                spacing="5",
                                width="100%",
                            ),
                        ),
                        top="auto",
                        right="auto",
                        height="100%",
                        width="20em",
                        padding="1.5em",
                        bg=rx.color("jade", 2),
                    ),
                    width="100%",
                ),
                direction="left",
            ),
            padding="1em",
        ),
    )