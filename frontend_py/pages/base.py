import reflex as rx
from frontend_py.components.navbar import navbar
from frontend_py.components.footer import footer_newsletter

def base_page(child: rx.Component ,*args,**kwargs) -> rx.Component:
    return rx.fragment(
        navbar(),
        rx.color_mode.button(),
        rx.box(
            child,
            text_align="centre", 
            id="box-content-area"
        ),
        footer_newsletter()
    )

