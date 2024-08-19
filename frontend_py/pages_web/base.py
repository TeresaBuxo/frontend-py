import reflex as rx
from frontend_py.components.navbar import navbar
from frontend_py.components.footer import low_footer

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

