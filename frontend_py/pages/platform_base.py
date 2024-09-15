import reflex as rx
from ..components.sidebar import sidebar
from ..components.footer import footer_newsletter,low_footer
from ..components.navbar_platform import navbar_platform
from frontend_py.components.navbar import navbar
from frontend_py.components.footer import low_footer
from ..states.auth_state import AuthState
from ..constants import urls
from .login import login_page

def platform_base(child: rx.Component ,*args,**kwargs) -> rx.Component:
    platform = rx.fragment(
            rx.hstack(
                sidebar(),
                rx.desktop_only(
                    rx.box(width="16em",),
                ),
                rx.vstack(
                    navbar_platform(),
                    rx.box(
                        child,
                        text_align="centre", 
                        id="box-content-area"
                    ),
                    low_footer(),
                    width="90%"
                )
            ),
        )
    return platform
    #rx.cond(
    #     AuthState.is_authenticated,
    #     platform,
    #     login_page()
    # )
