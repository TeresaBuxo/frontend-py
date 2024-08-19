"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from .pages_web import home,about,contact,community,login,signup
from .pages_platform import platform,platform_projects
from .constants import urls
from rxconfig import config

app = rx.App(
    theme=rx.theme(
        appearance="light", 
        has_background=True, 
        panel_background="solid",
        scaling="90%",
        radius="medium", 
        accent_color="teal"
    )
)
