import reflex as rx
from ..components.sidebar import sidebar
from ..components.footer import footer_newsletter,low_footer
from ..components.navbar_platform import navbar_platform
from ..components.navbar import navbar
from ..components.footer import low_footer
from ..states.auth_state import AuthState
from ..constants import urls

def base_page(child: rx.Component ,*args,**kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.box(
            child,
            text_align="centre", 
            id="box-content-area"
        ),
        low_footer()
    )
