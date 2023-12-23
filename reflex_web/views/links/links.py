import reflex as rx
from reflex_web.components import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("GitHub"),
        link_button("LinkedIn"),
        
    )