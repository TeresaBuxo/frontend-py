import reflex as rx
from ..components.sidebar import sidebar
from ..components.footer import footer_newsletter,low_footer
from ..components.navbar_platform import navbar_platform


def platform_base(child: rx.Component ,*args,**kwargs) -> rx.Component:
    return rx.fragment(
        rx.hstack(
            sidebar(),
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

