import reflex as rx
from reflex_web.components import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("GitHub","https://github.com/JordyV23"),
        link_button("LinkedIn","https://www.linkedin.com/in/jordy-jhv/"),
        width="100%"
    )